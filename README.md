# ugc-product-review-skill

A modular Agent Skill for creating realistic UGC product-review video concepts and AI video-generation prompts.

The skill is designed around **progressive disclosure**: agents load a small `SKILL.md` first, then read only the references needed for the current task. This keeps active context focused while still supporting product strategy, category-specific realism, model adaptation, campaigns, QA, repair, and performance learning.

## Repository layout

```text
ugc-product-review-skill/
├── README.md
├── CONTRIBUTING.md
├── AGENTS.md
├── .gitignore
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

## Why modular

A one-product prompt normally needs only:

```text
core
+ creative strategy
+ one product category
+ prompt compiler
```

Campaign logic, video QA, performance analysis, model adapters, and commercial-claims guidance stay out of context until needed.

## What the skill can do

- analyze a product and identify the strongest visual proof
- choose an appropriate UGC review archetype automatically
- design hooks, first frames, emotional arcs, hero moments, and shot graphs
- maintain product and creator consistency
- add category-specific hand and physics constraints
- generate one prompt, clip packs, batches, or full campaigns
- debug generated videos and repair prompts
- learn from real content-performance metrics
- avoid repetitive concepts through campaign coverage logic

## Agent Skills format

The canonical skill lives in:

```text
skills/ugc-product-review/SKILL.md
```

It uses YAML frontmatter with `name` and `description`, and keeps detailed material in sibling `references/` and `assets/` directories so compatible agents can load content progressively.

## Installation

Copy or symlink:

```text
skills/ugc-product-review/
```

into the skills directory used by your agent/client.

Because different coding agents use different project/global skill locations, keep this repository's canonical copy under `skills/` and map it into the location expected by your client.

## Example invocation

```text
Create a 12-second realistic UGC review video for this product.
```

The skill should autonomously:
1. understand the product,
2. choose the best angle,
3. identify the hero proof,
4. create the shot sequence,
5. generate a production-ready prompt,
6. suggest alternative concepts.

See `examples/` for more workflows.

## Design principles

- Visual proof > marketing claims
- Product consistency > cinematic complexity
- Physical plausibility > spectacle
- Human imperfection > commercial polish
- Load only what the current task requires

## Repository name

**`ugc-product-review-skill`**

## License

No license has been selected yet. Choose a license before broad public reuse if you want to explicitly grant reuse rights.
