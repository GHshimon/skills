#!/usr/bin/env bash
# skills/ 配下の全スキルを ~/.claude/skills/ にシンボリックリンクで配備する。
# 使い方: git clone 後にリポジトリ直下で ./install.sh
# 更新は git pull だけで反映される（リンクなのでコピー不要）。
set -euo pipefail

# Git Bash / MSYS の ln -s は既定でコピーを作るため、ネイティブシンボリックリンクを強制する。
# シンボリックリンクには開発者モードが必要。無効な環境では権限不要のジャンクション(mklink /J)に
# フォールバックする（どちらもリンクなので git pull だけで更新が反映される）。
IS_WINDOWS=0
case "$(uname -s)" in
  MINGW*|MSYS*)
    IS_WINDOWS=1
    export MSYS='winsymlinks:nativestrict'
    ;;
esac

# 既存のリンク/ジャンクションを安全に外す（実体ディレクトリの中身は消さない）
remove_link() {
  local dst="$1"
  [ -e "$dst" ] || [ -L "$dst" ] || return 0
  if [ "$IS_WINDOWS" = 1 ]; then
    # DirectoryInfo.Delete() は非再帰なので、ジャンクション/リンク自体だけを外せる
    powershell.exe -NoProfile -Command "(Get-Item '$(cygpath -w "$dst")').Delete()" 2>/dev/null && return 0
  fi
  rm -f "$dst" 2>/dev/null || true
}

# シンボリックリンク → (Windowsのみ) ジャンクション の順で試す
make_link() {
  local src="$1" dst="$2"
  remove_link "$dst"
  if ln -sn "$src" "$dst" 2>/dev/null; then
    return 0
  fi
  if [ "$IS_WINDOWS" = 1 ]; then
    powershell.exe -NoProfile -Command \
      "New-Item -ItemType Junction -Path '$(cygpath -w "$dst")' -Target '$(cygpath -w "$src")' -ErrorAction Stop | Out-Null" \
      >/dev/null 2>&1 && return 0
  fi
  return 1
}

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
  make_link "${d%/}" "$TARGET/$name" || {
    echo "ERROR: リンク作成に失敗: $name（シンボリックリンクは開発者モード、ジャンクションも不可の場合は権限を確認）" >&2
    exit 1
  }
  echo "linked: $TARGET/$name -> ${d%/}"
  linked=$((linked + 1))
done

# 常駐コア（CLAUDE.md）の配備。本リポジトリ由来でない既存ファイルは上書きしない
CORE_SRC="$REPO_DIR/core/CLAUDE.md"
CORE_DST="${HOME}/.claude/CLAUDE.md"
if [ -f "$CORE_SRC" ]; then
  if [ -f "$CORE_DST" ] && [ ! -L "$CORE_DST" ] && ! head -1 "$CORE_DST" | grep -q "AI Harness Core"; then
    echo "skip (手書きの CLAUDE.md を保護。core/CLAUDE.md と手動で統合してください): $CORE_DST"
  elif ln -sfn "$CORE_SRC" "$CORE_DST" 2>/dev/null; then
    echo "linked: $CORE_DST -> $CORE_SRC"
  else
    cp "$CORE_SRC" "$CORE_DST"
    echo "copied: $CORE_DST（ファイルリンク不可のためコピー配備。git pull 後は install.sh を再実行）"
  fi
fi

echo "完了: ${linked} スキルを配備。Claude Code を再起動するか /skills で読み込みを確認してください。"
