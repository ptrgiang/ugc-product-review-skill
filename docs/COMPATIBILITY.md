# Compatibility

The canonical skill follows the open Agent Skills format: a skill directory containing `SKILL.md` with YAML frontmatter and optional supporting resources.

## Recommended installer

Use the open `skills` CLI for cross-agent installation:

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

Exact paths may evolve, so use your client's current documentation or the `skills` CLI when possible.

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
- any unsupported feature or caveat
