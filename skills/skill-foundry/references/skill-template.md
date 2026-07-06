# SKILL.md テンプレート

新規スキルはこのテンプレートを複製して埋める。`{{ }}` をすべて置換したら
`python3 skills/skill-foundry/scripts/validate_skill.py <skill-dir>`（リポジトリ直下から） で検証する。

```markdown
---
name: {{skill-name}}
description: {{何をするスキルか}}。{{どんな依頼・状況のときに使用するか}}。
---

# {{Skill Title}}

## 役割（Role）
{{このスキルを使うときにエージェントが担う専門的立場}}

## 目的（Objective）
{{達成すべきゴール。測定可能に}}

## 制約（Constraints）
- {{守るべきルール。肯定文で}}
- {{定量値には根拠強度 🟢🟡⚪ を付す}}

## ツール（Tools）
- {{使用ツールと使用条件。単純作業は Sonnet 5 サブエージェントに委任}}

## 手順（Methodology）
1. {{3〜5段階に分割した手順}}
2. {{各段階の成果物}}

## 失敗例と対策（Pitfalls）
- **{{事象}}:** {{原因}} → **対策:** {{対策}}

## 完了条件（Completion Criteria）
{{終了の判断基準。例:「◯◯を3件提示し検証が通ったら終了」}}

## 出典
[`references/sources.md`](references/sources.md) を参照。
```

## 記入時の注意
- description は「何を + いつ」の2文構成。起動判定はこの欄だけで行われる
- 本文は判断手順に集中させ、長い背景知識は `references/` へ（progressive disclosure）
- 完了条件のないセクションを作らない
