#!/usr/bin/env python3
"""Build the three invocable skill bundles from one canonical source."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skill-src" / "criar-especificacao"
OUTPUT = ROOT / "skills"
ALIASES = {
    "criar-especificacao": {
        "display_name": "Criar Especificação WMS",
        "default_prompt": "Use $criar-especificacao para levantar, validar e gerar esta issue funcional do BeeStock.",
    },
    "criar": {
        "display_name": "Criar Jira WMS",
        "default_prompt": "Use $criar para levantar, validar e gerar esta issue funcional do BeeStock.",
    },
    "jira": {
        "display_name": "Jira BeeStock",
        "default_prompt": "Use $jira para levantar, validar e gerar esta issue funcional do BeeStock.",
    },
}


def replace_yaml_value(text: str, key: str, value: str, *, occurrence: int = 1) -> str:
    lines = text.splitlines()
    seen = 0
    for index, line in enumerate(lines):
        if line.lstrip().startswith(f"{key}:"):
            seen += 1
            if seen == occurrence:
                indentation = line[: len(line) - len(line.lstrip())]
                lines[index] = f'{indentation}{key}: "{value}"'
                return "\n".join(lines) + "\n"
    raise ValueError(f"Missing YAML key: {key}")


def render_bundle(name: str, destination: Path) -> None:
    metadata = ALIASES[name]
    shutil.copytree(SOURCE, destination)

    skill_path = destination / "SKILL.md"
    skill_text = skill_path.read_text(encoding="utf-8")
    skill_text = replace_yaml_value(skill_text, "name", name)
    skill_path.write_text(skill_text, encoding="utf-8")

    openai_path = destination / "agents" / "openai.yaml"
    openai_text = openai_path.read_text(encoding="utf-8")
    openai_text = replace_yaml_value(openai_text, "display_name", metadata["display_name"])
    openai_text = replace_yaml_value(openai_text, "default_prompt", metadata["default_prompt"])
    openai_path.write_text(openai_text, encoding="utf-8")


def build(destination_root: Path) -> None:
    destination_root.mkdir(parents=True, exist_ok=True)
    for name in ALIASES:
        destination = destination_root / name
        if destination.exists():
            shutil.rmtree(destination)
        render_bundle(name, destination)


def directories_equal(left: Path, right: Path) -> bool:
    comparison = filecmp.dircmp(left, right)
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    if any(not filecmp.cmp(left / name, right / name, shallow=False) for name in comparison.common_files):
        return False
    return all(directories_equal(left / name, right / name) for name in comparison.common_dirs)


def check() -> int:
    with tempfile.TemporaryDirectory(prefix="beestock-skill-build-") as temporary:
        expected = Path(temporary) / "skills"
        build(expected)
        if not OUTPUT.exists() or not directories_equal(expected, OUTPUT):
            print("Generated skill bundles are stale. Run: python scripts/build_skills.py")
            return 1
    print("Generated skill bundles are up to date.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated bundles are stale")
    args = parser.parse_args()
    if args.check:
        return check()
    build(OUTPUT)
    print("Built: " + ", ".join(ALIASES))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
