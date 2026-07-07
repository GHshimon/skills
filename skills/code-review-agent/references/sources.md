# 出典（Sources）

根拠強度: 🟢 一次/公式 / 🟡 複数二次で一致 / ⚪ 目安。
収集: 2026-07-07 skill-foundry ①リサーチ（Sonnet 5 サブエージェント、WebSearch 検証済み）。

## 欠陥検出

- 🟢 Google eng-practices, "What to look for in a code review"（中心的問い・並行処理・bikeshedding） — https://google.github.io/eng-practices/review/reviewer/looking-for.html
- 🟢 Code Complete / SEL 研究（コードリーディングの検出効率） — https://ptolemy.berkeley.edu/~johnr/info/reviews.html
- 🟢 Ousterhout, 複雑さの3症状・エラー処理 — https://web.stanford.edu/~ouster/cgi-bin/cs190-spring15/lecture.php?topic=errorHandling
- 🟢/🟡 Bacchelli & Bird (ICSE 2013), レビューの主便益は知識共有 — https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/
- 🟡 見逃しバグの分類（意味的バグ約51%） — https://arxiv.org/pdf/2205.09428

## 可読性・簡潔化

- 🟢 Google eng-practices, "The Standard of Code Review"（スタイルガイドが唯一の権威・Nit:） — https://google.github.io/eng-practices/review/reviewer/standard.html
- 🟢 Ousterhout, A Philosophy of Software Design（深い/浅いモジュール） — https://dev.to/gosukiwi/software-design-deep-modules-2on9
- 🟢 Fowler, "Beck Design Rules"（シンプル設計4ルールの優先順位） — https://martinfowler.com/bliki/BeckDesignRules.html
- 🟡 Cognitive Complexity — https://axify.io/blog/cognitive-complexity
- 🟡 過剰な DRY の弊害 — https://medium.com/@dr.daler.boboev/dry-code-vs-simple-solutions-unraveling-the-issues-of-too-dry-code-378c3dd0ea96

## 変更影響範囲

- 🟢 Google eng-practices, "Small CLs"（100行目安・自己完結した1変更） — https://google.github.io/eng-practices/review/developer/small-cls.html
- 🟢 Semantic Versioning（破壊的変更= MAJOR） — https://semver.org/
- 🟢 Ousterhout, information leakage — https://www.janmeppe.com/blog/a-philosophy-of-software-design-john-ousterhout/
- 🟡 blast radius / カナリア＋フィーチャーフラグ — https://www.harness.io/blog/canary-release-feature-flags

## コメントの伝え方

- 🟢 Conventional Comments（label/decoration・nitpick は non-blocking・praise） — https://conventionalcomments.org/
- 🟢 Google eng-practices, "How to write code review comments" — https://google.github.io/eng-practices/review/reviewer/comments.html
- 🟢 GitLab, "Code Review Guidelines"（blocking 明示の運用） — https://docs.gitlab.com/development/code_review/
- 🟡 nitpick 乱用の弊害 — https://blog.danlew.net/2021/02/23/stop-nitpicking-in-code-reviews/
