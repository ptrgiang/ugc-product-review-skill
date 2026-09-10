# ugc-product-review-skill

A modular Agent Skill for creating realistic UGC product-review video concepts and AI video-generation prompts.

[![Validate skill](https://github.com/ptrgiang/ugc-product-review-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/ptrgiang/ugc-product-review-skill/actions/workflows/validate-skill.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

The project is built around **progressive disclosure**: an agent reads a small `SKILL.md` router first, then loads only the references needed for the current task. This keeps active context focused while still supporting product strategy, category-specific realism, model adaptation, campaigns, QA, repair, and performance learning.

## Quick start

The canonical skill is:

```text
skills/ugc-product-review/SKILL.md
```

Copy or symlink the entire directory:

```text
skills/ugc-product-review/
```

into the skills location used by your agent or coding environment.

Then give the agent a request such as:

```text
Create a 12-second realistic UGC review video for this product.
```

The skill should autonomously identify the product, choose the strongest angle, design the hook and hero proof, and return a production-ready video prompt.

## What it can do

- analyze product references and identify the strongest visual proof
- choose an appropriate review archetype automatically
- design hooks, first frames, emotional arcs, hero moments, and shot graphs
- preserve creator and product consistency
- add category-specific hand and physics constraints
- generate single prompts, clip packs, batches, or campaigns
- review generated video results and repair prompts
- learn from real content-performance metrics
- reduce concept repetition through campaign coverage logic

## Progressive disclosure

A typical one-product prompt loads only:

```text
core
+ creative strategy
+ one product category
+ prompt compiler
```

Other modules stay out of context until needed:

- model adapters only when a target video model matters
- campaign logic only for multi-video planning
- QA/repair only when reviewing or fixing output
- performance learning only when real metrics are supplied
- commerce/claims only when commercial or factual-claim rules matter

## Repository layout

```text
ugc-product-review-skill/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── AGENTS.md
├── scripts/
│   └── validate_skill.py
├── .github/
│   ├── workflows/
│   │   └── validate-skill.yml
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── skills/
│   └── ugc-product-review/
│       ├── SKILL.md
│       ├── references/
│       │   ├── core.md
│       │   ├── creative-strategy.md
│       │   ├── prompt-compiler.md
│       │   ├── model-adapters.md
│       │   ├── campaign-engine.md
│       │   ├── qa-and-repair.md
│       │   ├── performance-learning.md
│       │   ├── commerce-and-claims.md
│       │   └── categories/
│       └── assets/
└── examples/
```

## Example workflows

**Single product review**

```text
Create a realistic 10-second UGC review video for this countertop appliance.
```

**Campaign**

```text
Create 10 distinct review-video concepts for this product. Avoid repeating hooks and hero moments.
```

**Repair**

```text
The generated video changes the product shape and the hands look wrong. Diagnose it and repair the prompt.
```

See `examples/` for more.

## Compatibility

The repository intentionally keeps the canonical skill vendor-neutral. It follows a portable Agent Skills pattern: a self-contained skill directory with `SKILL.md`, YAML frontmatter, optional references, and optional assets.

Different coding agents use different filesystem locations for skills. Keep the repository copy canonical and map `skills/ugc-product-review/` into the location expected by your client.

Model-specific prompting guidance is isolated in `references/model-adapters.md` so the main skill does not depend on one video generator.

## Validation

Run locally:

```bash
python scripts/validate_skill.py
```

GitHub Actions runs the same validation on pushes to `main` and on pull requests. The validator checks the canonical skill, required frontmatter, referenced modules, required files, and keeps the router from growing into a monolithic prompt file.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Repository-level guidance for coding agents lives in [AGENTS.md](AGENTS.md).

When adding new behavior, prefer a focused reference module with a clear trigger instead of expanding `SKILL.md` or loading extra context "just in case."

## Design principles

- Visual proof > marketing claims
- Product consistency > cinematic complexity
- Physical plausibility > spectacle
- Human imperfection > commercial polish
- Load only what the current task requires

## Versioning

The first public production-ready baseline is documented as **1.0.0** in [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE).
