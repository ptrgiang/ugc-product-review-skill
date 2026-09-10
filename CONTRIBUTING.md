# Contributing

Contributions are welcome. The project is intentionally modular so useful improvements can stay small and reviewable.

## Contribution principles

A change should improve at least one of:

- generation reliability
- product fidelity
- UGC realism
- creative diversity
- context efficiency
- cross-agent portability
- evaluation quality

Prefer a focused improvement over a broad rewrite.

## Where changes belong

- Router / activation behavior: `skills/ugc-product-review/SKILL.md`
- General production rules: `skills/ugc-product-review/references/core.md`
- Concept selection: `skills/ugc-product-review/references/creative-strategy.md`
- Prompt formatting: `skills/ugc-product-review/references/prompt-compiler.md`
- Product-specific behavior: `skills/ugc-product-review/references/categories/`
- Model-specific behavior: `skills/ugc-product-review/references/model-adapters.md`
- Campaign logic: `skills/ugc-product-review/references/campaign-engine.md`
- QA / repair: `skills/ugc-product-review/references/qa-and-repair.md`
- Metric-driven iteration: `skills/ugc-product-review/references/performance-learning.md`
- Commercial claims: `skills/ugc-product-review/references/commerce-and-claims.md`
- Cross-agent notes: `docs/COMPATIBILITY.md`

## Good first contributions

Good starter PRs include:

- one missing product category
- one reproducible product-interaction failure and repair
- one category-specific physics improvement
- one coding-agent compatibility note
- one campaign-diversity example
- one validation improvement

See `docs/ROADMAP.md` for more ideas.

## Development workflow

1. Fork the repository.
2. Create a focused branch.
3. Make the smallest change that solves the problem.
4. Run:

```bash
python scripts/validate_skill.py
```

5. Include a concrete example or reproduction when behavior changes.
6. Open a pull request using the repository template.

## Adding a category

A category module should contain only product-specific knowledge that meaningfully changes generation quality.

Include:

- interaction priorities
- valid product states when relevant
- physical/hand constraints
- strongest review archetypes
- hero moments
- targeted negative constraints

Do not copy generic rules already covered by `core.md`.

Then add the category path to `SKILL.md` routing only if the category is broad and reusable enough to justify permanent discovery text.

## Model-adapter changes

Treat video-model behavior as empirical, not permanent truth.

A model-adapter PR should preferably include:

- model/version tested
- example input
- observed failure or strength
- why the proposed instruction helps

Avoid undocumented pseudo-syntax unless it has been verified.

## AI-assisted contributions

AI-assisted contributions are welcome. If an AI agent materially generated or transformed the change, mention that in the pull request description and describe what you personally verified.

The submitter remains responsible for correctness, licensing, and test results.

## Pull request checklist

- Does the change belong in an existing module?
- Does it add context that most runs do not need?
- Can the new instruction be loaded only when relevant?
- Does it duplicate an existing rule?
- Does it invent product facts or unsupported model capabilities?
- Does it preserve visual-proof-first and physical-plausibility principles?
- Does `python scripts/validate_skill.py` pass?

## Community

Use issues for reproducible bugs and scoped feature proposals. Use pull requests for concrete changes. For security concerns, follow `SECURITY.md` rather than opening a public issue.
