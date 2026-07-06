# 出典（Sources）

本スキルの主張の裏付け。各項目に「根拠の強さ」を付す。
- 🟢 一次情報 / 公式ドキュメント
- 🟡 複数の二次情報で一致
- ⚪ 業界で語られる目安（要一次検証）

## コンテキスト/プロンプトエンジニアリング（セクション2・4）

- 🟢 Anthropic, "Effective context engineering for AI agents"
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  — コンテキストは有限資源であり、質を量に優先させる。just-in-time retrieval、コンパクション設計、サブエージェントへの調査隔離。
- 🟢 Anthropic, "Equipping agents for the real world with Agent Skills"
  https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
  — スキルの progressive disclosure（name/description のみ先読み）と SKILL.md 構造。
- 🟢 Claude Code Docs, "Best practices"
  https://code.claude.com/docs/en/best-practices
  — CLAUDE.md は軽量に保つ、計画と実行の分離、検証ループ。

## モデルの位置づけ（セクション5）

- 🟢 Anthropic, "Introducing Claude Fable 5 and Claude Mythos 5"
  https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
  — Fable 5 は 2026-06-09 一般提供開始。多数のベンチマークで SOTA。安全策として一部クエリは Claude Opus 4.8 が応答（＝両者は別モデル）。
- 🟢 Anthropic, "Models overview"
  https://platform.claude.com/docs/en/about-claude/models/overview
  — モデル系統と ID（claude-fable-5 / claude-opus-4-8）。

## McKinsey「Lilli」侵害（セクション1・3の事例）

- 🟢 McKinsey 公式声明, "Statement on strengthening safeguards within the Lilli tool"
  https://www.mckinsey.com/about-us/media/statement-on-strengthening-safeguards-within-the-lilli-tool
  — 当事者による一次確認（2026-07-06 追記: skill-foundry ①リサーチで発見し 🟡→🟢 に格上げ）。
- 🟡 BankInfoSecurity, "Autonomous Agent Hacked McKinsey's AI in 2 Hours"
  https://www.bankinfosecurity.com/autonomous-agent-hacked-mckinseys-ai-in-2-hours-a-31007
- 🟡 NeuralTrust, "How an AI Agent Hacked McKinsey and Exposed 46 Million Messages"
  https://neuraltrust.ai/blog/agent-hacked-mckinsey
- 🟡 1Kosmos, "McKinsey Lilli Breach (2026): What It Reveals About Agent Authentication"
  https://www.1kosmos.com/resources/blog/mckinsey-lilli-breach-agent-authentication
  — 2026年3月。自律型攻撃エージェントが約2時間で SQL インジェクション経由の読み書き権限を取得。約4,650万メッセージ・728,000ファイル・57,000アカウント・95システムプロンプトが露出。22の公開エンドポイントが認証不要だった。

## ⚪ 一次検証を推奨する定量値（本文で「目安」と明記）

- 「AIパイロットの過半数が本番スケールに失敗」「準備・クレンジングに労力の40〜50%」「タスク分割で作業時間◯%短縮」「並列化で最大◯%高速化」等。
  これらは業界の解説でよく語られるが、出所が揺れる。文脈の説明には有用だが、意思決定の根拠にする際は自組織のデータや一次調査で裏を取ること。
