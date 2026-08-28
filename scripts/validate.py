#!/usr/bin/env python3
"""Validate structure, references, and cross-harness contracts."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_NAMES = {"criar-especificacao", "criar", "jira"}
REQUIRED_REFERENCES = {
    "references/evidence-and-state.md",
    "references/interview.md",
    "references/jira-format.md",
    "references/audit-rubric.md",
    "references/learning-loop.md",
    "references/examples/melhoria.md",
    "references/examples/bug.md",
    "references/examples/resumido.md",
}


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def validate_bundle(bundle: Path) -> list[str]:
    errors: list[str] = []
    skill_path = bundle / "SKILL.md"
    if not skill_path.exists():
        return [f"{bundle}: missing SKILL.md"]
    text = skill_path.read_text(encoding="utf-8")
    try:
        metadata = frontmatter(text)
    except ValueError as error:
        return [f"{skill_path}: {error}"]

    if metadata.get("name") != bundle.name:
        errors.append(f"{skill_path}: name must match directory")
    if not metadata.get("description"):
        errors.append(f"{skill_path}: description is required")
    if metadata.get("disable-model-invocation") != "true":
        errors.append(f"{skill_path}: must be explicitly invoked")
    if "TODO" in text:
        errors.append(f"{skill_path}: unresolved TODO")
    for phrase in ("## Máquina de estados", "## Modos de profundidade", "## Revisão independente"):
        if phrase not in text:
            errors.append(f"{skill_path}: missing {phrase}")
    for reference in REQUIRED_REFERENCES:
        if not (bundle / reference).exists():
            errors.append(f"{bundle}: missing {reference}")

    for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", text):
        if not (bundle / target).exists():
            errors.append(f"{skill_path}: broken reference {target}")

    openai_yaml = bundle / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        errors.append(f"{bundle}: missing agents/openai.yaml")
    else:
        openai_text = openai_yaml.read_text(encoding="utf-8")
        if "allow_implicit_invocation: false" not in openai_text:
            errors.append(f"{openai_yaml}: explicit invocation policy missing")
        if f"${bundle.name}" not in openai_text:
            errors.append(f"{openai_yaml}: default prompt must mention ${bundle.name}")
    return errors


def main() -> int:
    build_check = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_skills.py"), "--check"],
        cwd=ROOT,
        check=False,
    )
    errors: list[str] = []
    actual_names = {path.name for path in SKILLS.iterdir() if path.is_dir()} if SKILLS.exists() else set()
    if actual_names != EXPECTED_NAMES:
        errors.append(f"skills/: expected {sorted(EXPECTED_NAMES)}, got {sorted(actual_names)}")
    for name in sorted(EXPECTED_NAMES):
        errors.extend(validate_bundle(SKILLS / name))
    if build_check.returncode:
        errors.append("generated bundles are stale")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Validation passed for Codex, Claude Code, DeepSeek Harness, and Hermes Harness bundles.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
