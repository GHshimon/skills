#!/usr/bin/env bash
# skills/ 配下の全スキルを ~/.claude/skills/ にシンボリックリンクで配備する。
# 使い方: git clone 後にリポジトリ直下で ./install.sh
# 更新は git pull だけで反映される（リンクなのでコピー不要）。
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${HOME}/.claude/skills"
mkdir -p "$TARGET"

linked=0
for d in "$REPO_DIR"/skills/*/; do
  name="$(basename "$d")"
  if [ ! -f "${d}SKILL.md" ]; then
    echo "skip (SKILL.md なし): $name"
    continue
  fi
  python3 "$REPO_DIR/skills/skill-foundry/scripts/validate_skill.py" "${d%/}" >/dev/null || {
    echo "skip (validate FAIL): $name"
    continue
  }
  ln -sfn "${d%/}" "$TARGET/$name"
  echo "linked: $TARGET/$name -> ${d%/}"
  linked=$((linked + 1))
done

echo "完了: ${linked} スキルを配備。Claude Code を再起動するか /skills で読み込みを確認してください。"
