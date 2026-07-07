# 起動精度の回帰テスト（Trigger Cases）

想定発話 → 起動すべきスキルの対応表。棚卸し（/skill-inventory）時に、
各発話を description 群と照合し「一意にそのスキルへ辿り着けるか」を判定する。
スキルを追加・description を変更したら、このファイルにケースを追加すること（各スキル最低2件）。

判定基準: ◯=一意に起動 / △=競合あり（要 description 調整） / ×=起動しない

| # | 想定発話 | 期待スキル | 備考 |
| --- | --- | --- | --- |
| 1 | UI設計エージェント用のスキルを作りたい | skill-foundry | |
| 2 | 既存スキルが肥大化したので分割したい | skill-foundry | |
| 3 | CLAUDE.md をレビューして性能を引き出したい | ai-agent-architect | |
| 4 | マルチエージェント構成の設計を相談したい | ai-agent-architect | system-design と競合しないこと（AI環境=architect / 業務システム=system-design） |
| 5 | この業務はAI化できるか仕分けしてほしい | dx-consult-agent | |
| 6 | PoC から本番に進めるべきか判断して | dx-consult-agent | |
| 7 | この画面のデザインをレビューして | ui-design-agent | ux-review と競合しないこと（見た目/設計=ui / 使いやすさ監査=ux） |
| 8 | デザイントークンを設計して | ui-design-agent | |
| 9 | ユーザビリティ監査をして | ux-review-agent | |
| 10 | このフローが使いにくい原因を診断して | ux-review-agent | |
| 11 | マイクロサービスに分割すべきか判断して | system-design-agent | |
| 12 | この機能のスケール戦略を設計して | system-design-agent | |
| 13 | ブランドガイドラインを作りたい | brand-design-agent | |
| 14 | サイトとSNSでトンマナがばらばらなので統一したい | brand-design-agent | |
| 15 | この PR をレビューして | code-review-agent | |
| 16 | レビューコメントの書き方を改善したい | code-review-agent | |
| 17 | Teams に自動通知を飛ばしたい | notification-operator | |
| 18 | アラートがうるさいので整理して | notification-operator | |
| 19 | この開発の流れを note 記事にして | note-narrative-editor | |
| 20 | 対話ログを物語風にまとめて | note-narrative-editor | |

## 負例（どのスキルも起動すべきでない発話）

誤発動（false positive）の検出用。これらの発話でいずれかのスキルが起動する判定になったら、
該当スキルの description が広すぎる。

| # | 発話 | 誤発動しがちなスキル（警戒対象） |
| --- | --- | --- |
| N1 | この関数のバグを直して | code-review-agent（レビュー依頼ではない） |
| N2 | ブログに載せる技術解説記事を書いて | note-narrative-editor（ナラティブ変換ではない） |
| N3 | このボタンの色を青に変えて | ui-design-agent（設計・監査ではない単純作業） |
| N4 | データベースのクエリが遅いので直して | system-design-agent（アーキテクチャ判断ではない） |
| N5 | 会議の議事録をまとめて | note-narrative-editor / dx-consult-agent |
| N6 | エラーメッセージの文言を分かりやすくして | ux-review-agent / brand-design-agent（監査・設計依頼ではない） |
