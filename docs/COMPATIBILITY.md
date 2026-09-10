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
- Codex: `.codex/skills/` or the Codex global skills directory
- Universal / several compatible agents: `.agents/skills/`

Exact paths may evolve, so prefer the `skills` CLI, `gh skill`, or your client's current documentation.

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
