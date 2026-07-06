#!/usr/bin/env python3
"""PostToolUse hook: SKILL.md が編集されたら validate_skill.py を実行する。

stdin に Claude Code のフックイベント JSON を受け取る。外部コマンド（jq 等）に
依存しないため、Windows / macOS / Linux で同一に動作する。
FAIL 時は exit 2 で編集セッションにエラー内容をフィードバックする。
"""
import json
import os
import subprocess
import sys


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    file_path = (data.get("tool_input") or {}).get("file_path") or ""
    if not file_path.replace("\\", "/").endswith("/SKILL.md"):
        return 0
    validator = os.path.join(os.path.dirname(os.path.abspath(__file__)), "validate_skill.py")
    result = subprocess.run(
        [sys.executable, validator, os.path.dirname(file_path)],
        capture_output=True,
    )
    if result.returncode != 0:
        # validate_skill.py は UTF-8 で出力する。コンソール既定(cp932等)での再デコードを避ける
        sys.stderr.buffer.write(result.stdout + result.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
