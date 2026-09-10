# Maintainer Guide

## Review order

When reviewing a pull request:

1. confirm the change belongs in the proposed module,
2. reject duplicated generic guidance,
3. check whether the rule can be loaded lazily,
4. require reproducible evidence for model-specific claims,
5. run `python scripts/validate_skill.py`,
6. confirm examples and docs still match routing behavior.

## Release discipline

Use semantic versions for public releases:

- PATCH — wording, examples, or narrow fixes without behavioral contract changes
- MINOR — new category, workflow, adapter, or backward-compatible capability
- MAJOR — routing or output changes that can materially change existing use

Update `CHANGELOG.md` before tagging a release.

## Contribution quality

Prefer PRs that contain one clear unit of value.

Large generated PRs should be split when independent parts can be reviewed separately.

AI-assisted changes are acceptable, but the contributor should state what they personally verified.

## Repository health

Periodically review:

- stale model-adapter guidance
- broken install commands
- missing category coverage
- recurring issue patterns
- duplicated instructions
- oversized reference modules
- CI failures
- security reports

## Growth without bloat

Community growth should expand evidence, examples, integrations, and focused modules rather than grow the root `SKILL.md`.
