# 出典（Sources）— dx-consult-agent

skill-foundry ①リサーチ（Sonnet 5 サブエージェント4機、2026-07-06 実施）の採用知見。
- 🟢 一次情報 / 公式
- 🟡 複数の二次情報で一致
- ⚪ 目安（意思決定には自社データでの検証を推奨）

## A. DX戦略・失敗要因

- 🟢 BCG「6成功要因」— 統合戦略・経営コミット・人材・アジャイルガバナンス・進捗管理・モジュール型IT基盤の充足で成功率が大幅に向上（30%→80%と報告）。
  https://www.bcg.com/publications/2024/reaching-purpose-driven-digital-transformation-success
- 🟢 MIT CISR「企業AI成熟度4段階」— Stage2（PoC構築）→Stage3（全社運用体制）への移行が財務インパクトの分岐点。
  https://cisr.mit.edu/publication/2025_0801_EnterpriseAIMaturityUpdate_WoernerSebastianWeillKaganer
- 🟢 McKinsey「Why digital strategies fail」— DX施策の約70%が目標未達。原因は技術ではなく文化・変革管理。ツール先行導入への警告も同稿。
  https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/why-digital-strategies-fail
- 🟢 McKinsey「Pilot purgatory」— パイロットから全社スケールできる製造業は3割未満。
  https://www.mckinsey.com/~/media/mckinsey/business%20functions/operations/our%20insights/how%20digital%20manufacturing%20can%20escape%20pilot%20purgatory/digital-manufacturing-escaping-pilot-purgatory.pdf
- 🟢 McKinsey（Jon Garcia対談）— 意思決定オーナーシップの不明確さが変革失敗の根本原因。
  https://www.mckinsey.com/capabilities/transformation/our-insights/common-pitfalls-in-transformations-a-conversation-with-jon-garcia
- 🟢 Deloitte「State of AI in the Enterprise」(2025, n=3,235) — 経営層主導のAIガバナンス設計組織のほうが高い事業価値。
  https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html
- ⚪ 「文化投資で成功率5.3倍」「生成AIパイロットで成果は5%」等の流通統計 — 出所が揺れるため目安扱い。

## B. Workflow / Agent 設計

- 🟢 Anthropic「Building effective agents」— Workflow（事前定義コードパス）と Agent（LLMが動的制御)の定義、「最もシンプルな解から始める」原則、5パターン（Prompt Chaining / Routing / Parallelization / Orchestrator-Workers / Evaluator-Optimizer）。
  https://www.anthropic.com/research/building-effective-agents
- 🟢 Anthropic「Multi-agent research system」— orchestrator-worker 構成で単一モデル比 90.2% の性能向上、ただしトークン消費は通常チャット比約15倍。高価値タスクに限定すべき。
  https://www.anthropic.com/engineering/multi-agent-research-system
- 🟡 Workflow固定/Agent裁量の切り分け基準 — ルールが列挙可能で安定→Workflow、曖昧・変化頻繁・文脈解釈→Agent。
  https://arxiv.org/pdf/2602.10122 ほか複数実務解説で一致
- 🟡 HITL三段階モデル — 可逆=自動承認 / 取消可能=通知 / 不可逆=承認ゲート。承認疲れ回避のためゲートは高影響時に限定し、「何を/なぜ/何が変わる/どう取り消すか」を提示。
  https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo /
  https://machinelearningmastery.com/building-a-human-in-the-loop-approval-gate-for-autonomous-agents/

## C. 変革マネジメント・暗黙知

- 🟢 Prosci ADKAR — Awareness/Desire/Knowledge/Ability/Reinforcement。個人フォーカスの変革モデル（「成果6倍」はベンダー調査値のため目安として扱う）。
  https://www.prosci.com/blog/adkar-model
- 🟡 Kotter 8段階 — リーダーシップ・感情面の統合に強いが完遂に時間を要し急速な変革には不向き。
  https://www.prosci.com/blog/kotters-change-management-theory
- 🟡 AIチャンピオン制度 — 現場ベテランを起点にした段階展開が外部講師型より定着（「採用率2.1倍」「職務別研修67% vs 汎用23%」はベンダー報告値＝目安）。
  https://aiassemblylines.com/post/ai-champions-program-enterprise-adoption / https://iternal.ai/ai-change-management
- 🟢 ナレッジエリシテーション（Springer, 査読論文）— 暗黙知の外部化は専門家との協働プロセスが核心。
  https://link.springer.com/article/10.1007/s44163-022-00020-w
- 🟡 プロセスマイニングの限界 — 知識集約型プロセスの暗黙知捕捉には限界、理論駆動の解釈が必要。
  https://ideas.repec.org/p/pdn/dispap/148.html
- 🟢 Gartner — インセンティブ不整合と共同設計欠如が失敗最大要因。生成AIプロジェクトの半数がPoC後に中止。
  https://www.gartner.com/en/articles/genai-project-failure
- 🟡 LSE ケーススタディ — 現場負担を増やす設計で熱意が回避に転じた失敗例（現場不在の要件定義）。
  https://blogs.lse.ac.uk/businessreview/2026/03/18/the-story-of-one-failed-digital-transformation/
- 🟡 ビッグバン導入の危険 — 退行の多くが導入後72時間以内に表面化、シャドー運用で予防可能との指摘。
  https://www.digitalapplied.com/blog/agentic-ai-anti-patterns-10-ways-teams-botch-deployment-2026

## D. ガバナンス・リスク

- 🟢 NIST AI RMF — Govern / Map / Measure / Manage の4機能。Govern は全体を横断。
  https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ / https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
- 🟢 EU AI Act — 禁止/ハイリスク/透明性義務/最小の4階層。禁止慣行は2025-02、GPAI規則は2025-08発効。
  https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- 🟡 附属書IIIハイリスクの適用期限延期（2026-08→2027-12、Digital Omnibus合意）— 施行状況は変動するため相談時に必ず最新確認。
  https://axis-intelligence.com/eu-ai-act-news/
- 🟢 McKinsey「Lilli」公式声明 — 2026-03、自律攻撃エージェントが未認証エンドポイント＋SQLインジェクション経由で約2時間で読み書き権限を取得。
  https://www.mckinsey.com/about-us/media/statement-on-strengthening-safeguards-within-the-lilli-tool
- 🟢 OWASP「AI Agent Security Cheat Sheet」/ Agentic Top 10 — プロンプトインジェクション・過剰な自律性・ツール不正利用・メモリポイズニング。
  https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- ⚪ 最小権限・デフォルト拒否・監査ログ粒度などの実務プラクティス集。
  https://www.knostic.ai/blog/ai-governance-best-practices / https://elevateconsult.com/insights/7-ai-governance-best-practices-for-enterprise-ai-teams/
