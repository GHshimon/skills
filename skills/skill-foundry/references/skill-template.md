# SKILL.md テンプレート — プロファイル選択ガイド

新規スキルは、まず**実行者のプロファイル**を選び、対応テンプレートを複製して埋める。
`{{ }}` をすべて置換したら `python3 skills/skill-foundry/scripts/validate_skill.py <skill-dir>`（リポジトリ直下から）で検証する。

## プロファイル選択

| プロファイル | 実行者 | 向いているスキル | テンプレート |
| --- | --- | --- | --- |
| **Manager** | メインセッション / Opus サブエージェント | タスク分解・受け入れ判定・レビュー・方針決定など**判断が支配的**な業務 | [skill-template-manager.md](skill-template-manager.md) |
| **Worker** | Sonnet 5 サブエージェント（コールドスタート） | 収集・整形・変換・検証など**手順が支配的**な業務 | [skill-template-worker.md](skill-template-worker.md) |

判断基準: 「手順を完全に列挙できるか?」— できるなら Worker、途中に裁量的判断が残るなら Manager。
1スキルに両方が混ざったら、判断部分を Manager に残し、手順部分を Worker スキルとして分割する（skill-foundry 第④段階）。

## 両プロファイル共通の規約

- frontmatter: `name`（64字以内・小文字数字ハイフン・予約語 `anthropic`/`claude` 禁止・ディレクトリ名と一致）、`description`（1024字以内）
- **description は自然言語のトリガー文で書く**（「何をするか」+「いつ使うか」の2文構成）。起動判定はモデルがこの文章を読んで行うため、ここだけは構造化・記号化しない
- モデルへの紐付けはスキルではなく**エージェント定義**が持つ（[model-routing.md](model-routing.md) 参照）。frontmatter 直後に想定実行者を1行明記する
- 定量値には根拠強度 🟢🟡⚪ を付し、出典は `references/sources.md` に分離する
- 本文は判断・手順に集中させ、長い背景知識は `references/` へ（progressive disclosure）
- 完了条件のないセクションを作らない
