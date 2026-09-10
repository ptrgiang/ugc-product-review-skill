# Architecture

## Goal

Keep the active context small while preserving production depth.

The repository uses progressive disclosure:

1. an agent discovers `name` and `description`,
2. it loads `SKILL.md` only after activation,
3. it loads focused references only when a task requires them.

## Runtime routing

```text
USER TASK
   |
   +-- one product / one prompt
   |     core + creative strategy + one category + prompt compiler
   |
   +-- batch / campaign
   |     core + creative strategy + one category + campaign engine
   |
   +-- generated video QA
   |     core + QA/repair (+ one category if physics matters)
   |
   +-- prompt repair
   |     core + QA/repair + prompt compiler
   |
   +-- performance metrics
         core + performance learning + campaign engine
```

Optional modules are loaded only when they materially change the answer:

- `model-adapters.md` — target video model matters
- `commerce-and-claims.md` — commercial/testimonial/claim-sensitive content

## Source-of-truth boundaries

`SKILL.md` owns activation, routing, defaults, and quality gates.

`references/core.md` owns general product-review production rules.

Category files own product-specific interaction and physics knowledge.

Campaign, QA, performance, and model behavior should remain isolated in their dedicated modules.

## Contribution rule

Before adding an instruction, ask:

1. Is it needed on nearly every run? Put it in `core.md`.
2. Is it specific to one workflow? Put it in that workflow module.
3. Is it specific to one product type? Put it in a category module.
4. Is it vendor-specific? Keep it in an optional adapter or agent metadata file.
5. Is it just an example? Put it under `examples/` rather than the canonical skill.

## Complexity budget

Prefer shallow references from `SKILL.md` to focused files. Avoid chains where one reference tells the agent to load several more references.

The project intentionally avoids a single exhaustive prompt handbook because irrelevant instructions can reduce generation quality and make agent behavior harder to predict.
