#!/usr/bin/env python3
"""Agent Skill 形式バリデータ。

使い方: python3 validate_skill.py <skill-dir> [<skill-dir> ...]
検証項目: SKILL.md の存在 / frontmatter / name 規則 / description 規則。
仕様: Anthropic Agent Skills（name<=64字・小文字数字ハイフン・予約語禁止、
description 非空・<=1024字・「何を+いつ」）。
"""
import os
import re
import sys

RESERVED = ("anthropic", "claude")
WHEN_CUES = ("使用する", "使う", "とき", "Use when", "use this")


def validate(skill_dir: str) -> list[str]:
    errors = []
    path = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(path):
        return [f"{skill_dir}: SKILL.md がない（フラットな .md はスキルとして認識されない）"]

    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return [f"{path}: YAML frontmatter がない"]
    fm = m.group(1)

    def field(key):
        mm = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
        return mm.group(1).strip() if mm else None

    name = field("name")
    desc = field("description")

    if not name:
        errors.append(f"{path}: name がない")
    else:
        if len(name) > 64:
            errors.append(f"{path}: name が64字超（{len(name)}字）")
        if not re.fullmatch(r"[a-z0-9-]+", name):
            errors.append(f"{path}: name に小文字・数字・ハイフン以外の文字")
        if any(w in name for w in RESERVED):
            errors.append(f"{path}: name に予約語（{'/'.join(RESERVED)}）")
        if name != os.path.basename(os.path.abspath(skill_dir)):
            errors.append(f"{path}: name '{name}' がディレクトリ名と不一致")

    if not desc:
        errors.append(f"{path}: description がない")
    else:
        if len(desc) > 1024:
            errors.append(f"{path}: description が1024字超（{len(desc)}字）")
        if not any(c in desc for c in WHEN_CUES):
            errors.append(f"{path}: description に「いつ使うか」の記述が見当たらない")

    for key in ("name", "description"):
        v = field(key)
        if v and re.search(r"<[^>]+>", v):
            errors.append(f"{path}: {key} に XML タグ")

    return errors


def main() -> int:
    targets = sys.argv[1:]
    if not targets:
        print(__doc__)
        return 2
    all_errors = []
    for t in targets:
        errs = validate(t)
        all_errors.extend(errs)
        print(("FAIL " if errs else "PASS ") + t)
        for e in errs:
            print("  - " + e)
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
