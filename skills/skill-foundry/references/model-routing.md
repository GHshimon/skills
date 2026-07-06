# モデルルーティング規約 — スキル・エージェント・標準機能の対応

大原則: **新しい仕組みを作る前に「Claude Code 標準機能で可能か」を必ず確認し、
標準機構で実現できるものを自作しない。**

## 標準機能マッピング

やりたいこと → 使う標準機構。この表にあるものを独自実装したら設計ミスとみなす。

| やりたいこと | 標準機構 |
| --- | --- |
| 常駐させる基本方針・絶対制約 | `CLAUDE.md` + `settings.json` の permissions（allow/deny） |
| 能力のオンデマンドロード | Agent Skills（description のみ常駐、本文は発動時ロード） |
| 作業担当を Sonnet 5 で動かす | エージェント定義 `.claude/agents/<name>.md` の `model: sonnet` |
| 管理者を Opus で動かす | メインセッションのモデル選択 / `Agent` tool の `model: opus` |
| 段階ごとのモデル切り替え | Workflow の `agent(prompt, {model, effort})` |
| アクションをトリガーに検証を走らせる | hooks（PreToolUse / PostToolUse / Stop 等）+ 決定論的スクリプト |
| 破壊的操作の防止 | permissions の deny ルール、サンドボックスモード、git worktree 分離 |

## モデル紐付けの原則

- **スキルはモデルに紐づかない**（SKILL.md に実行モデルを指定するフィールドはない）。
  紐付けは呼び出し側＝エージェント定義・Agent tool・Workflow が持つ
- スキル側は「想定実行者」を本文冒頭に1行明記し、Manager / Worker プロファイルで書き分ける
  （[skill-template.md](skill-template.md) 参照）
- 役割分担のデフォルト: **判断・統合・受け入れ = Opus / メインセッション**、
  **収集・整形・検証などの手順作業 = Sonnet 5 サブエージェント**（skill-foundry の委任規則と同一）

## エージェント定義テンプレート

Worker を常設する場合は `.claude/agents/<name>.md` に置く:

```markdown
---
name: {{agent-name}}
description: {{どんなタスクをこのエージェントに委任するか（呼び出し判断はこの文で行われる）}}
model: sonnet
tools: {{必要最小限のツール（例: Read, Grep, Glob, Bash）}}
---

{{システムプロンプト。使用する Worker スキル名と、入力契約・出力契約の要点を書く}}
```

- `model:` は Worker なら `sonnet`、レビュー担当なら `opus`
- `tools:` は最小権限で列挙する（Worker に Write が不要なら与えない)

## フックの役割（マイクロ・フック）

フックは**軽量ルーティングに徹する**。フック自体にロジックを持たせない。

- フックにできること: 決定論的スクリプトの実行 / ツール実行のブロック / コンテキストの注入
- フックに**できない**こと: スキルの直接起動（「検証スキルを呼ぶ」は、検証スクリプトを直接実行するか、
  「◯◯スキルを使え」という指示を注入するかのどちらかで実現する）
- 実例: 本リポジトリの PostToolUse フック（SKILL.md 編集 → `validate_skill.py` 自動実行）が模範形
