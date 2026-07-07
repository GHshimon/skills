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
| [`ui-design-agent`](skills/ui-design-agent/SKILL.md) | UI設計の判断基準集（Manager）。情報階層・レイアウト/グリッド・コンポーネント選定・ビジュアル調和を M3 / HIG / WCAG / ゲシュタルトで設計・監査。 |
| [`ux-review-agent`](skills/ux-review-agent/SKILL.md) | ユーザビリティ監査（Manager）。Nielsen 10 / NN/g 深刻度5段階 / WCAG 2.2 AA / ダークパターン5分類による違反検出と優先順位付け。 |
| [`system-design-agent`](skills/system-design-agent/SKILL.md) | アーキテクチャ判断基準集（Manager）。境界の切り方・スケール戦略・データ一貫性（CAP/PACELC）・ADR によるトレードオフ記録。 |
| [`brand-design-agent`](skills/brand-design-agent/SKILL.md) | ブランド一貫性監査（Manager）。VI 4点監査・Voice/Tone 設計（NN/g 4次元）・ガイドライン策定・リブランド判断。 |
| [`code-review-agent`](skills/code-review-agent/SKILL.md) | コードレビュー判断基準集（Manager）。Google eng-practices / Ousterhout / Conventional Comments に基づく欠陥検出・影響評価・severity 区分コメント。 |
| [`notification-operator`](skills/notification-operator/SKILL.md) | 通知モジュール構築の手順書（Worker/Sonnet 5）。Google SRE の要否判定・集約設計・Teams(Workflows)/Slack 実装パターン。 |
| [`note-narrative-editor`](skills/note-narrative-editor/SKILL.md) | 開発過程を note 記事用の自己内省ナラティブへ変換する手順書（Worker/Sonnet 5）。事実改変禁止・素材対応表付き。 |

配備対象のスキルはすべて `skills/` 配下に置く。`_incoming/` は claude.ai からの回収待ち置き場（配備対象外）。

## スキルの検証

新規・更新スキルは必ず形式検証を通す:

```bash
python3 skills/skill-foundry/scripts/validate_skill.py <skill-dir> [...]
```

`.claude/settings.json` の PostToolUse Hook により、Claude Code 上で SKILL.md を編集すると自動で同じ検証が走る（FAIL はその場でフィードバックされる）。

## 配備（リポジトリ → 実行環境）

このリポジトリが単一の正（source of truth）。配備は3経路:

1. **PC の Claude Code**: `git clone` して `./install.sh` を実行（`skills/*` を `~/.claude/skills/` にシンボリックリンク。以後 `git pull` だけで更新反映）。Windows は Git Bash で実行（開発者モード無効時はジャンクション/コピーに自動フォールバック）
4. **Cursor**: `.cursorrules` は手書きせず `python3 scripts/generate_cursorrules.py [出力先]` で生成する（core/CLAUDE.md 全文＋スキル目次。本文はタスク時に読み込ませる方式）。core またはスキルを変更したら再生成する
2. **claude.ai**: 各 `SKILL.md` を claude.ai > 設定 > 機能 > スキル にアップロード
3. **プラグイン**: Claude Code で `/plugin marketplace add GHshimon/skills` → `ai-company-skills` をインストール（`.claude-plugin/` マニフェスト経由の1コマンド配布）

## claude.ai スキルの回収

claude.ai にしか本文がない自作スキル（`astro-web` / `vite-react-web` / `nextjs-web`）は `_incoming/` に受け皿を用意済み:

1. claude.ai のスキル編集画面から本文をコピー
2. `_incoming/<name>/SKILL.md` の「回収待ち」見出し以下を本文で置き換える
3. `git mv _incoming/<name> skills/<name>` で配備対象に昇格（Hook が自動検証）

## 常駐コア（core/CLAUDE.md）

常駐するルールは [`core/CLAUDE.md`](core/CLAUDE.md) の1枚のみ（約20行）。基本方針・品質ゲート・対話プロトコル・絶対制約だけを置き、能力の詳細はスキル側に分離する。`install.sh` が `~/.claude/CLAUDE.md` へ配備する（手書きの既存ファイルは保護）。

## 設計原則

- **標準機能ファースト:** 仕組みを新設する前に「Claude Code 標準機能で可能か」を確認し、標準機構（skills / agents / hooks / permissions）で実現できるものを自作しない。対応表は [`model-routing.md`](skills/skill-foundry/references/model-routing.md)。
- **2プロファイル設計:** スキルは Manager（判断系・Opus 実行）と Worker（手順系・Sonnet 5 サブエージェント実行）で書き分ける。テンプレートは [`skill-template.md`](skills/skill-foundry/references/skill-template.md) から選択。
- **完成度評価:** スキルは [`eval-rubric.md`](skills/skill-foundry/references/eval-rubric.md) の10軸で Opus が採点し、「配備可」（16点以上・0点なし）のものだけを配備する。採点はクリエイト完了時・アップデート後・棚卸し時のチェックポイントで行う。

## 自動運用（Autonomous Operation）

無人でループを回すための装置。設計の経緯は Opus レビュアー2体との議論で確定（2026-07-07）。

- **安全柵（多層防御）:** ①GitHub ブランチ保護（main への force push / 削除を機械的に拒否 — 最も実効性のある層）②[.claude/settings.json](.claude/settings.json) の permissions（秘密情報の Read deny ＋破壊的コマンドの ask。※プレフィックス方式は抜け穴があり得るため補助層と位置づける）③core/CLAUDE.md の行動原則（モデル判断層）
- **独立採点:** [`agents/skill-scorer.md`](agents/skill-scorer.md)（Opus・読み取り専用）。独立性はコールドスタートの別セッションで担保する
- **棚卸し:** [`commands/skill-inventory.md`](commands/skill-inventory.md)（/skill-inventory）。validate → 独立採点（バッチ・再開可能）→ 起動精度チェック → 失敗還元 → 鮮度確認 → 記録。月次のスケジュール実行（cloud routine）から呼ぶ
- **失敗還元のデータフロー（一方向）:** [`FAILURE_LOG.md`](FAILURE_LOG.md)（生ログ）→ skill-foundry ③ → [`DEBT_INVENTORY.md`](DEBT_INVENTORY.md)（構造化記録）
- **起動精度の回帰テスト:** [`tests/trigger-cases.md`](tests/trigger-cases.md)（正例20＋負例6）
- **クラウドへのコア注入:** [`hooks/hooks.json`](hooks/hooks.json) の SessionStart フック。`~/.claude/CLAUDE.md` に常駐コアが既にある環境（PC）では注入をスキップして二重化を防ぐ

**リリース手順（手動・低頻度のため自動化しない）:** ①スキル変更を main にマージ ②`plugin.json` の version を上げてプッシュ（クラウドは次回セッションから反映）③PC は `git pull && ./install.sh` ④claude.ai チャットは該当スキルの zip を再アップロード

## メンテナンス

- スキルの棚卸し結果は [`DEBT_INVENTORY.md`](DEBT_INVENTORY.md) を参照。
- 新規スキルは上記構造に従い、`description` の起動条件と出典（`references/`）を必ず添える。
