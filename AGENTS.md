# AGENTS.md

## Repository purpose

This repository contains an Agent Skill for realistic UGC product-review video planning and prompt generation.

## Canonical skill

`skills/ugc-product-review/SKILL.md`

## Editing rules

- Keep `SKILL.md` concise and focused on routing, default workflow, and quality gates.
- Put detailed domain knowledge in `references/`.
- Prefer one focused reference file over growing the root skill.
- Do not duplicate the same rule across several references unless repetition is required for independent loading.
- Add product-category knowledge under `references/categories/`.
- Add reusable non-instruction artifacts under `assets/`.
- Keep examples outside the canonical skill folder unless the skill itself must load them.
- New modules must have a clear trigger condition in `SKILL.md`.
- Do not add a module that is loaded "just in case."

## Compatibility goal

Favor the portable Agent Skills convention:
- a self-contained skill directory
- required `SKILL.md`
- YAML frontmatter containing at least `name` and `description`
- optional references and assets loaded only when relevant

Avoid coupling the canonical skill to one vendor-specific tool unless placed in an optional integration file.

## Quality

Before merging a skill change:
1. confirm routing still loads the minimum references,
2. confirm product facts are not invented,
3. confirm prompt outputs prioritize visual proof and physical plausibility,
4. confirm campaign modules do not leak into single-prompt tasks,
5. confirm QA modules are not loaded unless reviewing/repairing outputs.
