# Compatibility

The canonical skill follows the open Agent Skills format: a skill directory containing `SKILL.md` with YAML frontmatter and optional supporting resources.

## Recommended installers

### Option A — open `skills` CLI

Use the open `skills` CLI for broad cross-agent installation:

```bash
npx skills@latest add ptrgiang/ugc-product-review-skill --skill ugc-product-review
```

Global install:

```bash
npx skills@latest add ptrgiang/ugc-product-review-skill --skill ugc-product-review -g
```

Target one or more supported agents:

```bash
npx skills@latest add ptrgiang/ugc-product-review-skill \
  --skill ugc-product-review \
  -a claude-code \
  -a codex
```

The `skills` CLI supports many coding agents and handles their project/global paths. Prefer it over duplicating vendor-specific copies in this repository.

### Option B — GitHub CLI

Recent GitHub CLI versions include the preview `gh skill` command.

Preview the skill before installation:

```bash
gh skill preview ptrgiang/ugc-product-review-skill ugc-product-review
```

Install for a coding agent:

```bash
gh skill install ptrgiang/ugc-product-review-skill ugc-product-review --agent claude-code
gh skill install ptrgiang/ugc-product-review-skill ugc-product-review --agent codex
```

Install at user scope:

```bash
gh skill install ptrgiang/ugc-product-review-skill ugc-product-review --agent codex --scope user
```

For reproducible installs, pin a release tag or commit SHA with `--pin` after releases are published.

Repository maintainers can also use:

```bash
gh skill publish --dry-run
```

to validate skill discovery before publishing workflows.

## Manual installation

Copy:

```text
skills/ugc-product-review/
```

into the skill directory used by your client.

Common examples include:

- Claude Code: `.claude/skills/` or `~/.claude/skills/`
- Codex: `.codex/skills/`, `.agents/skills/`, or the current Codex global skills directory depending on installation method
- Universal / several compatible agents: `.agents/skills/`

Exact paths may evolve, so prefer the `skills` CLI, `gh skill`, or your client's current documentation.

## Verified compatibility results

Test date: 2026-09-10.

### Claude Code — Sonnet 5, caveman mode

Status: **PASS for activation and progressive reference loading**.

Observed routing:

- single product prompt: `core.md`, `creative-strategy.md`, `categories/appliances.md`, `prompt-compiler.md`
- campaign concepts only: `core.md`, `creative-strategy.md`, `categories/appliances.md`, `campaign-engine.md`
- repair/diagnosis task: `core.md`, `qa-and-repair.md`, `prompt-compiler.md`

The first two routes matched the intended lazy-loading behavior. The repair route loaded `prompt-compiler.md` even though the request asked only for diagnosis and targeted repair instructions; the router has since been tightened so diagnosis-only requests should avoid the prompt compiler unless a revised generation prompt is requested.

Output quality was strong overall, with explicit product-confidence handling, category-specific reasoning, campaign coverage checks, standardized QA tags, and targeted repair guidance.

### Codex — GPT-5.6 Terra, medium and high

Status: **PASS for skill activation, PARTIAL for progressive reference loading**.

Observed behavior in all three smoke tests:

- Codex found and used the installed `ugc-product-review` skill.
- Codex reported reading only `SKILL.md` and did not open the routed reference files.
- As a result, outputs were plausible but more generic and less constrained than the Claude Code outputs.

Examples of drift from the intended routing included:

- inventing a specific product subtype such as an air fryer or portable blender when only a generic countertop appliance was described
- omitting the expected category/module-specific production structure
- using generic repair heuristics without actually loading `qa-and-repair.md`

The root `SKILL.md` has been updated with an explicit **reference-loading contract**: when a route lists references, agents must open those files before answering and must not claim a file was used unless it was actually read.

Codex should be re-tested after reinstalling or refreshing the skill.

## Smoke-test protocol

Use the same three prompts across agents so results are comparable:

1. single 12-second appliance review prompt
2. 10-concept campaign without full prompts
3. generated-video diagnosis / targeted repair only

Record:

- client and model/version
- installed skill path
- reference files actually opened
- whether the expected route matched
- notable output-quality differences

A test is considered fully passing when:

- the skill activates,
- the required references are actually opened,
- unrelated references remain unloaded,
- the output follows the intended production behavior.

## OpenAI / Codex metadata

`skills/ugc-product-review/agents/openai.yaml` provides optional OpenAI-specific interface metadata. The canonical `SKILL.md` does not depend on it.

## Compatibility policy

The repository aims to keep the skill portable by:

- requiring only standard `name` and `description` frontmatter
- avoiding vendor-specific tool syntax in the canonical workflow
- isolating model-specific prompt guidance in `references/model-adapters.md`
- using relative paths for skill resources
- keeping scripts optional to normal skill execution

## Adding compatibility

If a coding agent supports the Agent Skills format, prefer documenting installation rather than committing a generated duplicate of the skill.

Add vendor-specific files only when they provide real functionality that cannot be represented portably.

When proposing a compatibility PR, include:

- agent/client name and version
- install location or command
- minimal invocation used to verify activation
- whether progressive reference loading worked
- any unsupported feature or caveat
