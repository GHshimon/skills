# 出典（Sources）

根拠強度: 🟢 一次/公式 / 🟡 複数二次で一致 / ⚪ 目安。
収集: 2026-07-07 skill-foundry ①リサーチ（Sonnet 5 サブエージェント、WebSearch 検証済み）。

## 境界の切り方

- 🟢 Martin Fowler, "BoundedContext" — https://martinfowler.com/bliki/BoundedContext.html
- 🟡 microservices.io, "Decompose by business capability" — https://microservices.io/patterns/decomposition/decompose-by-business-capability.html
- 🟢 Sam Newman, "Building Microservices 2nd Edition" — https://samnewman.io/books/building_microservices_2nd_edition/
- 🟡 AWS DevOps Blog, "Microservice decomposition using Conway's Law" — https://aws.amazon.com/jp/blogs/devops/microservice-decomposition-using-conways-law/
- 🟢 AWS Well-Architected, "Serverless Applications Lens: Decomposing a monolith" — https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/decomposing-a-monolith.html

## スケール戦略

- 🟢 Kleppmann, "Designing Data-Intensive Applications" ch.1（負荷の記述）/ ch.6（パーティショニング） — https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/ch01.html
- 🟢 AWS Well-Architected, "Performance Efficiency Pillar" — https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/performance-efficiency-pillar.html
- 🟢 GCP, "Architecture Framework: Scalability" — https://cloud.google.com/architecture/framework/system-design/scalability
- 🟡 AWS, "Caching Best Practices" — https://aws.amazon.com/caching/best-practices/
- 🟡 Microsoft, "Azure architecture anti-patterns"（早すぎるスケーリング） — https://learn.microsoft.com/en-us/azure/architecture/antipatterns/

## データ設計（一貫性・耐障害性）

- 🟢 Gilbert & Lynch, "Brewer's conjecture (CAP)" — https://dl.acm.org/doi/10.1145/564585.564601
- 🟢 Abadi, "PACELC" — https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf
- 🟢 Kleppmann, "Designing Data-Intensive Applications"（一貫性モデル） — https://dataintensive.net/
- 🟢 AWS Well-Architected, "Reliability Pillar" — https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/reliability-pillar.html
- 🟢 AWS Reliability Pillar, "Retry with exponential backoff"（べき等性） — https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rest-safely-retry-with-exponential-backoff.html
- 🟡 microservices.io, "Saga" / "Database per Service" — https://microservices.io/patterns/data/saga.html / https://microservices.io/patterns/data/database-per-service.html

## トレードオフの記録（ADR）

- 🟢 Michael Nygard, "Documenting Architecture Decisions" — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- 🟢 adr.github.io（MADR テンプレート・ステータス管理） — https://adr.github.io/
- 🟢 AWS Prescriptive Guidance, "Architectural Decision Records" / "Best practices"（オーナー設置・定例レビュー） — https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/welcome.html
- 🟢 ThoughtWorks Technology Radar, "Lightweight Architecture Decision Records"（Adopt、コード管理下に保存） — https://www.thoughtworks.com/en-us/radar/techniques/lightweight-architecture-decision-records
- 🟡 ADR 形骸化（Decision Documentation Theater）の指摘 — https://hidekazu-konishi.com/entry/architecture_decision_records_templates_and_operations.html
- 🟡 2PC のブロッキング問題 — https://hosseinnejati.medium.com/the-two-phase-commit-problem-why-distributed-transactions-are-hard-80fd2f16aebf
- 🟢 GCP, "Disaster recovery planning guide"（RTO/RPO 起点の設計） — https://cloud.google.com/architecture/disaster-recovery
