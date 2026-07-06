# skills

Claude 向けの Agent Skills を管理するリポジトリ。

## 構造

各スキルは **ディレクトリ + `SKILL.md`** で構成する（フラットな `*.md` はスキルとして認識されない）。

```
<skill-name>/
  SKILL.md          # 必須。YAML frontmatter (name, description) + 本文
  references/       # 任意。文脈に読み込む補足ドキュメント
  scripts/          # 任意。実行コード
  assets/           # 任意。出力に使うファイル
```

### SKILL.md frontmatter の規約

- `name`: 必須。64文字以内、小文字・数字・ハイフンのみ。予約語 `anthropic` / `claude` を含めない。ディレクトリ名と一致させる
- `description`: 必須。1024文字以内。「**何をする**スキルか」と「**いつ使う**か」の両方を書く（起動判定はこの記述に依存する）

参考: Anthropic "Equipping agents for the real world with Agent Skills" / Claude Platform Docs "Agent Skills"。

## 収録スキル

| スキル | 概要 |
| --- | --- |
| [`ai-agent-architect`](ai-agent-architect/SKILL.md) | AIエージェント設計・プロンプト/コンテキストエンジニアリング・運用・失敗回避の知識ベース。CLAUDE.md レビューやモデルの性能を引き出す設計に使う。 |
| [`skill-foundry`](skill-foundry/SKILL.md) | 専門エージェント用スキルを鍛造するメタスキル。①リサーチ→②クリエイト→③アップデート→④分割の4段階パイプラインと Sonnet 5 サブエージェント委任規則。AI Company のエージェント編成は [`references/agent-roster.md`](skill-foundry/references/agent-roster.md) 参照。 |

## スキルの検証

新規・更新スキルは必ず形式検証を通す:

```bash
python3 skill-foundry/scripts/validate_skill.py <skill-dir> [...]
```

## メンテナンス

- スキルの棚卸し結果は [`DEBT_INVENTORY.md`](DEBT_INVENTORY.md) を参照。
- 新規スキルは上記構造に従い、`description` の起動条件と出典（`references/`）を必ず添える。
