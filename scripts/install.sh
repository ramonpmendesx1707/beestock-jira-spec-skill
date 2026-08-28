#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill_names=(criar-especificacao criar jira)

declare -A target_roots=(
  [agents]="${HOME}/.agents/skills"
  [claude]="${HOME}/.claude/skills"
  [hermes]="${HERMES_HOME:-${HOME}/.hermes}/skills"
)

selected=(agents claude hermes)
if [[ $# -gt 0 ]]; then
  selected=()
  for option in "$@"; do
    case "$option" in
      --all) selected=(agents claude hermes) ;;
      --codex|--deepseek) selected+=(agents) ;;
      --claude) selected+=(claude) ;;
      --hermes) selected+=(hermes) ;;
      *) echo "Unknown option: $option" >&2; exit 2 ;;
    esac
  done
fi

for target_key in "${selected[@]}"; do
  target_root="${target_roots[$target_key]}"
  mkdir -p "$target_root"
  for skill_name in "${skill_names[@]}"; do
    source_path="${repo_root}/skills/${skill_name}"
    target_path="${target_root}/${skill_name}"
    if [[ -e "$target_path" && ! -L "$target_path" ]]; then
      echo "Refusing to replace non-symlink: $target_path" >&2
      exit 1
    fi
    ln -sfn "$source_path" "$target_path"
    echo "linked $skill_name -> $target_root"
  done
done

echo "Installation complete. Restart the harness if the skills do not appear immediately."
