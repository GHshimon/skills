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
| [`ai-agent-architect`](skills/ai-agent-architect/SKILL.md) | AIエージェント設計・プロンプト/コンテキストエンジニアリング・運用・失敗回避の知識ベース。CLAUDE.md レビューやモデルの性能を引き出す設計に使う。 |
| [`dx-consult-agent`](skills/dx-consult-agent/SKILL.md) | DX・AI導入コンサルタント知識ベース。業務のAI適用仕分け（Workflow/Agent/人間）、PoC→本番移行判断、変革マネジメント、AIガバナンス設計。skill-foundry パイプラインの第1号成果物。 |
| [`skill-foundry`](skills/skill-foundry/SKILL.md) | 専門エージェント用スキルを鍛造するメタスキル。①リサーチ→②クリエイト→③アップデート→④分割の4段階パイプラインと Sonnet 5 サブエージェント委任規則。AI Company のエージェント編成は [`references/agent-roster.md`](skills/skill-foundry/references/agent-roster.md) 参照。 |

配備対象のスキルはすべて `skills/` 配下に置く。`_incoming/` は claude.ai からの回収待ち置き場（配備対象外）。

## スキルの検証

新規・更新スキルは必ず形式検証を通す:

```bash
python3 skills/skill-foundry/scripts/validate_skill.py <skill-dir> [...]
```

`.claude/settings.json` の PostToolUse Hook により、Claude Code 上で SKILL.md を編集すると自動で同じ検証が走る（FAIL はその場でフィードバックされる）。

## 配備（リポジトリ → 実行環境）

このリポジトリが単一の正（source of truth）。配備は3経路:

1. **PC の Claude Code**: `git clone` して `./install.sh` を実行（`skills/*` を `~/.claude/skills/` にシンボリックリンク。以後 `git pull` だけで更新反映）
2. **claude.ai**: 各 `SKILL.md` を claude.ai > 設定 > 機能 > スキル にアップロード
3. **プラグイン**: Claude Code で `/plugin marketplace add GHshimon/skills` → `ai-company-skills` をインストール（`.claude-plugin/` マニフェスト経由の1コマンド配布）

## claude.ai スキルの回収

claude.ai にしか本文がない自作スキル（`astro-web` / `vite-react-web` / `nextjs-web`）は `_incoming/` に受け皿を用意済み:

1. claude.ai のスキル編集画面から本文をコピー
2. `_incoming/<name>/SKILL.md` の「回収待ち」見出し以下を本文で置き換える
3. `git mv _incoming/<name> skills/<name>` で配備対象に昇格（Hook が自動検証）

## メンテナンス

- スキルの棚卸し結果は [`DEBT_INVENTORY.md`](DEBT_INVENTORY.md) を参照。
- 新規スキルは上記構造に従い、`description` の起動条件と出典（`references/`）を必ず添える。
