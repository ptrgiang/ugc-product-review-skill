# Contributing

Contributions are welcome.

## Principles

Changes should improve at least one of:
- generation reliability
- product fidelity
- UGC realism
- creative diversity
- context efficiency
- cross-agent portability

## Where changes belong

- Router / activation behavior: `skills/ugc-product-review/SKILL.md`
- General production rules: `references/core.md`
- Concept logic: `references/creative-strategy.md`
- Prompt formatting: `references/prompt-compiler.md`
- Product-specific behavior: `references/categories/`
- Model-specific behavior: `references/model-adapters.md`
- Campaign logic: `references/campaign-engine.md`
- QA / repair: `references/qa-and-repair.md`
- Metric-driven iteration: `references/performance-learning.md`
- Commercial claims: `references/commerce-and-claims.md`

## Pull request checklist

- Does the change belong in an existing module?
- Does it increase context unnecessarily?
- Can the new instruction be loaded only when needed?
- Does it conflict with another module?
- Does it introduce unsupported factual claims about a video model?
- Does it preserve the skill's visual-proof-first philosophy?
