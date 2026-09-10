# Google Flow real-video evaluation

This protocol evaluates whether prompts produced by `ugc-product-review` survive real video generation, not merely whether an agent routes to the correct reference files.

Do not treat a visually attractive output as a pass if product identity, controls, hand interaction, or the hero proof fails.

## Evaluation sequence

Run cases in this order:

1. appliance multi-state interaction
2. liquid / material physics
3. targeted repair from a failed generation

Use the same input/reference assets when comparing prompt revisions. Change one prompt variable at a time whenever possible.

## What to record for every generation

Record:

- case id
- date
- generation model shown in Flow
- model/version label if visible
- generation mode/settings that materially affect the result
- input/reference assets used
- prompt revision (`V01`, `V02`, ...)
- generated output or representative frames
- pass/fail per QA dimension
- observed failure tags
- repair made for the next revision

Do not infer hidden model parameters or undocumented capabilities.

## Core scoring

Score each dimension 0, 1, or 2:

- **Product fidelity** — shape, proportions, materials, controls, lid/container geometry
- **Creator continuity** — creator appearance and wardrobe remain coherent where visible
- **Physical plausibility** — weight, support, contact, hinges/latches, liquid/material behavior
- **Hand quality** — grip, finger count/shape, contact and manipulation remain believable
- **State continuity** — product moves through plausible states without unexplained mutation
- **Hero clarity** — strongest visible proof is readable and held long enough
- **UGC realism** — looks like believable creator footage rather than polished commercial imagery
- **Prompt adherence** — major requested actions, framing, timing, and exclusions are respected

Maximum: 16.

### Baseline interpretation

- **14–16:** strong pass; suitable as a showcase candidate
- **11–13:** usable but needs targeted repair before showcasing
- **8–10:** weak; repair the highest-severity failures first
- **0–7:** regenerate from a simplified shot plan rather than patching many symptoms

A P0 product-identity or impossible-physics failure prevents a showcase pass regardless of total score.

## Repair discipline

For each failed revision:

1. identify the smallest set of root-cause failure tags
2. preserve everything that already worked
3. change only the instructions responsible for the failure
4. regenerate using the same references/model when possible
5. compare before/after on the same QA dimensions

The goal is not to find one lucky generation. The goal is to demonstrate that the skill can diagnose and improve reproducible failure modes.

## Showcase requirement

A public showcase case should contain:

- input/reference summary
- selected creative angle
- production prompt
- first generated result or representative frames
- QA diagnosis
- targeted repair
- repaired result
- concise before/after evaluation

Never fabricate model outputs, scores, or improvements. Only publish evidence from real generated results.
