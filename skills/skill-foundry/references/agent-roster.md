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
| 通知・連携 | `notification-operator` | 通知の要否 / 宛先・メンション制御 / 頻度設計 | アラート疲れ対策、Teams/Slack 通知設計プラクティス |
| note編集 | `note-narrative-editor` | プロジェクトの過程・対話の自己内省ナラティブへの変換 | ストーリーテリング構造、note 人気記事の型 |

## 工程ロールの吸収先（AI Harness Design マスター定義書より統合）

マスター定義書の工程別ロールは、独立エージェントにせず既存機構に吸収する（ロスターの二重化を防ぐ）。

| 定義書のロール | 吸収先 |
| --- | --- |
| Protocol Engineer | Worker スキルの**入力契約** + skill-foundry 委任規則（Manager の責務として遂行） |
| Workflow Architect | `dx-consult-agent`（業務分解）+ `system-design-agent`（構造設計） |
| Implementation Specialist | メインセッション（Manager）の実装統括。専用エージェント不要 |
| Quality Controller | Opus 独立レビュー + 完成度ルーブリック（[eval-rubric.md](eval-rubric.md)）採点 |
| Code Generator / Debug & Refactor Tester | Worker スキル（Sonnet 5）。必要になった案件で鍛造する |
| Notification Operator | 上表 `notification-operator`（Worker スキル1個で足りる） |
| Documentation & Dedicated Editor | **2分割**: 仕様書作成 Worker + 上表 `note-narrative-editor` |
| UI/UX Art Director | `ui-design-agent` / `ux-review-agent`（下記チェックリストが鍛造の種） |

## ui-design-agent / ux-review-agent 鍛造用: UI品質チェックリスト（ドラフト）

マスター定義書から採用・事実修正済み。鍛造時（skill-foundry ①リサーチ）に出典を `sources.md` へ確定させる。
名称は「UI品質チェックリスト」とし、スキル完成度ルーブリック（10軸）とは**別物**として扱う。

1. **コントラスト:** WCAG AA = 通常テキスト 4.5:1、大テキスト 3:1（🟢 W3C）
2. **クリック/タップ領域:** 目標水準を宣言して適用 — WCAG 2.5.8 AA = 24px / WCAG AAA・Apple HIG = 44px（🟢）
3. **デザイントークン一貫性:** 色・サイズのハードコード禁止、変数（トークン）参照のみ（🟡 デザインシステム慣行）
4. **空間設計:** 余白・要素サイズは 8px グリッドの倍数（⚪ 業界慣習）
5. **認知負荷:** 1画面の主要情報チャンクは 4±1（⚪ Cowan のワーキングメモリ研究由来の目安）

## 運用メモ
- スキル名は小文字・数字・ハイフンのみ（予約語 `anthropic`/`claude` 不可）
- 1エージェント=1スキルから始め、肥大化したら skill-foundry の第④段階で分割する
- 各スキルの `references/sources.md` に上記「思想の例」の実際の出典URLと根拠強度（🟢🟡⚪）を記録する
