# 出典（Sources）

根拠強度: 🟢 一次/公式 / 🟡 複数二次で一致 / ⚪ 目安。
収集: 2026-07-07 skill-foundry ①リサーチ（Sonnet 5 サブエージェント、WebSearch 検証済み）。

## アラート設計原則

- 🟢 Google SRE Book, "Monitoring Distributed Systems"（urgent/actionable/user-visible、3階層、症状ベース） — https://sre.google/sre-book/monitoring-distributed-systems/
- 🟢 Google SRE Book, "Practical Alerting"（アラート判定の4つの問い） — https://sre.google/sre-book/practical-alerting/
- 🟡 Four Golden Signals と SLO 連動 — https://sre.google/workbook/alerting-on-slos/

## アラート疲れ

- 🟡 SOC 実証研究（高再現率ルールと認知容量の構造的緊張） — https://dl.acm.org/doi/10.1145/3723158
- 🟡 医療 EHR 通知の無視率95%超（JAMA 2024 系） — https://pmc.ncbi.nlm.nih.gov/articles/PMC11845892/
- 🟡 相関エンジン・抑制・動的ベースライン — https://incident.io/blog/alert-fatigue-solutions-for-dev-ops-teams-in-2025-what-works
- 🟢 PagerDuty, Alert Grouping（dedup_key・時間窓5分初期値） — https://support.pagerduty.com/main/docs/intelligent-alert-grouping

## Slack

- 🟢 Slack, "App design guidelines"（全体メンション稀少・宛先選択・ダイジェスト） — https://docs.slack.dev/surfaces/app-design/
- 🟢 Slack, Incoming Webhooks / chat.postMessage 使い分け — https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/
- 🟢 Slack, Rate Limits（毎秒1メッセージ/チャンネル、429+Retry-After） — https://docs.slack.dev/apis/web-api/rate-limits/

## Microsoft Teams

- 🟢 Microsoft, Office 365 コネクタ廃止（2026-05 無効化）と Workflows 移行 — https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/
- 🟢 Microsoft, Power Automate での Adaptive Card 作成 — https://learn.microsoft.com/en-us/power-automate/create-adaptive-cards
- 🟢 Microsoft, Workflows の MessageCard 受付状況（2025-12 時点） — https://learn.microsoft.com/en-us/answers/questions/5685899/status-of-legacy-messagecard-support-in-workflows
