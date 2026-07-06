# AI Company エージェント編成（Agent Roster)

skill-foundry が育成対象とする専門エージェントと、それぞれのスキル命名・リサーチ起点。
「①リサーチ」の判断業務の言語化は、この表の「中核判断」から始める。

| エージェント | スキル名（予定） | 中核判断（リサーチ起点） | 最初に当たる思想・体系の例 |
| --- | --- | --- | --- |
| UI設計 | `ui-design-agent` | 情報階層 / レイアウト / コンポーネント選定 | デザインシステム（Material, HIG）、Refactoring UI、ゲシュタルト原則 |
| UXレビュー | `ux-review-agent` | ユーザビリティ違反の検出と重み付け | Nielsen 10 Heuristics、Norman『誰のためのデザイン?』、WCAG |
| システム設計 | `system-design-agent` | 境界の切り方 / スケール戦略 / トレードオフ明示 | DDD、Designing Data-Intensive Applications、AWS/GCP Well-Architected |
| TouchDesigner | `touchdesigner-agent` | ノードネットワーク設計 / GPU最適化 / リアルタイム演出 | Derivative公式Wiki、GLSL/コンピュートシェーダ実践、インタラクティブアート事例 |
| DXコンサル | `dx-consult-agent` | 業務の判断ポイント文書化 / Workflow+Agent 配分 | ai-agent-architect スキル（本リポジトリ）、McKinsey/BCG のDXフレーム |
| ブランドデザイン | `brand-design-agent` | ブランド一貫性 / トーン&マナー / VI規定 | Marty Neumeier『The Brand Gap』、ブランドガイドライン実例集 |
| コードレビュー | `code-review-agent` | 欠陥検出 / 可読性・簡潔化 / 変更影響範囲 | Google Engineering Practices、Code Complete、A Philosophy of Software Design |

## 運用メモ
- スキル名は小文字・数字・ハイフンのみ（予約語 `anthropic`/`claude` 不可）
- 1エージェント=1スキルから始め、肥大化したら skill-foundry の第④段階で分割する
- 各スキルの `references/sources.md` に上記「思想の例」の実際の出典URLと根拠強度（🟢🟡⚪）を記録する
