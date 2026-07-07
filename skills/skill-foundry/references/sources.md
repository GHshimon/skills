# 出典（Sources）

skill-foundry の規約・手法の裏付け。根拠強度: 🟢 一次/公式 / 🟡 二次一致 / ⚪ 目安。

## スキル形式と progressive disclosure

- 🟢 Anthropic, "Equipping agents for the real world with Agent Skills"
  https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
  — `<name>/SKILL.md` 構造、frontmatter（name/description）、description による起動判定、
  本文はオンデマンドロード（progressive disclosure）。
- 🟢 Claude Platform Docs, "Agent Skills"
  https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
  — name 64字以内・小文字数字ハイフン・予約語禁止、description 1024字以内の形式仕様。

## パイプライン設計（委任・検証・剪定）

- 🟢 Anthropic, "Effective context engineering for AI agents"
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  — コンテキストは有限資源。調査のサブエージェント隔離、結論だけ返させる委任、質 > 量。
- 🟢 Claude Code Docs, "Best practices"
  https://code.claude.com/docs/en/best-practices
  — 検証ループ（変更前後比較）、CLAUDE.md/常駐コンテキストの軽量化、計画と実行の分離。

## ⚪ 目安として運用する値

- 本文500行での分割トリガー、想定発話3つでの起動確認、ルーブリック配点（16点/0点なし）は
  本リポジトリの運用初期値であり、外部標準ではない。運用実績で調整する。
