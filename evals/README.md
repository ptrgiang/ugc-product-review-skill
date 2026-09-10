# Evaluation Framework

The `evals/` directory contains small, reproducible behavior fixtures for the canonical UGC Product Review skill.

The goal is not to benchmark a language model with a single numeric score. The goal is to catch regressions in routing, creative decisions, product-specific constraints, and campaign diversity as the skill evolves.

## Fixture structure

Each fixture is a JSON object with:

- `id` — stable fixture identifier
- `category` — primary product category
- `request` — representative user request
- `product_context` — minimal facts or visual assumptions supplied to the agent
- `expected_modules` — references the skill should load
- `forbidden_modules` — references that should stay unloaded for this task
- `expected_behavior` — high-level creative or QA decisions
- `critical_constraints` — requirements that must survive prompt compilation
- `failure_conditions` — outcomes that indicate a regression

## What CI validates

`python scripts/validate_evals.py` checks fixture structure, uniqueness, module paths, category routes, and basic progressive-disclosure rules.

This is a structural eval layer. Behavioral execution across real coding agents is tracked separately in `docs/COMPATIBILITY.md` and future agent smoke-test reports.

## Adding a fixture

Keep fixtures small and focused. One fixture should test one major production risk or routing decision. Prefer a clear regression case over a broad showcase example.
