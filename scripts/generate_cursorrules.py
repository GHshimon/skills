#!/usr/bin/env python3
"""core/CLAUDE.md とスキル一覧から .cursorrules を生成する。

.cursorrules は手書きしない（生成物）。単一の正は core/CLAUDE.md と skills/*/SKILL.md。
Cursor にはスキルのオンデマンドロード機構がないため、常駐コア全文＋「スキル目次」
（起動条件と参照先パス）だけを書き出し、本文はタスク時に該当ファイルを読ませる方式で
progressive disclosure を再現する。

使い方: python3 scripts/generate_cursorrules.py [出力先ディレクトリ]
        出力先省略時はリポジトリ直下に .cursorrules を生成する。
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def frontmatter_field(text: str, key: str) -> str:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ""
    mm = re.search(rf"^{key}:\s*(.+)$", m.group(1), re.M)
    return mm.group(1).strip().strip('"') if mm else ""


def main() -> int:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else REPO
    core_path = os.path.join(REPO, "core", "CLAUDE.md")
    core = open(core_path, encoding="utf-8").read().strip()

    rows = []
    skills_dir = os.path.join(REPO, "skills")
    for name in sorted(os.listdir(skills_dir)):
        p = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(p):
            continue
        desc = frontmatter_field(open(p, encoding="utf-8").read(), "description")
        trigger = desc.split("。")[0][:120]
        rows.append(f"- **{name}**: {trigger}。→ 該当タスクの前に `skills/{name}/SKILL.md` を読み込むこと")

    lines = [
        "<!-- AUTO-GENERATED — 手動編集禁止 -->",
        "<!-- 生成元: core/CLAUDE.md + skills/*/SKILL.md (https://github.com/GHshimon/skills) -->",
        "<!-- 再生成: python3 scripts/generate_cursorrules.py -->",
        "",
        core,
        "",
        "## スキル目次（オンデマンドロード）",
        "以下は目次のみ。本文を常駐させないこと。該当するタスクを始める前に、対応する SKILL.md を読み込む。",
        *rows,
        "",
    ]
    content = "\n".join(lines)
    out = os.path.join(out_dir, ".cursorrules")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"generated: {out} ({len(content.encode('utf-8'))} bytes, skills: {len(rows)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
