# Changelog

All notable changes to this project are documented here.

## [1.1.0] - 2026-09-16

### Added
- Optional slash-command preset layer with 80 textual creative presets organized into 8 progressive-disclosure groups.
- Presets for product/e-commerce, fashion, people/character, brand/marketing, social content, video/cinema, horror/supernatural, and document visuals.
- A slash-command router that loads only the matching preset group instead of injecting the full library into context.
- Explicit precedence rules so slash presets cannot override product/creator locks, physical plausibility, factual constraints, or claim/compliance rules.

### Changed
- `SKILL.md` can now route explicit slash-style inputs such as `/productshot`, `/characterref`, `/hookframe`, `/storyboard`, and `/continuityframe` while preserving the normal UGC production routes.
- Slash presets are treated as composable intent modifiers rather than platform-native commands or replacements for the core creative reasoning pipeline.

## [1.0.0] - 2026-09-10

### Added
- Modular Agent Skill architecture with progressive disclosure.
- Autonomous UGC review concept selection and prompt generation.
- Product-category reference modules for appliances, fashion, beauty, home utility, electronics, food and beverage, tools/DIY, and pet products.
- Campaign diversification, QA/repair, performance-learning, model-adapter, and commerce/claims modules.
- Creative registry and QA templates.
- Cross-agent repository guidance through `AGENTS.md` and contribution rules.

### Design principles
- Visual proof over marketing claims.
- Product fidelity over cinematic complexity.
- Physical plausibility over spectacle.
- Human imperfection over commercial polish.
