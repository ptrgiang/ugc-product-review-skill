#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ugc-product-review"
SKILL = SKILL_DIR / "SKILL.md"
PLUGIN = ROOT / "plugin.json"
OPENAI = SKILL_DIR / "agents" / "openai.yaml"

errors = []
warnings = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


# Canonical Agent Skill
if not SKILL.exists():
    fail(f"Missing canonical skill: {SKILL.relative_to(ROOT)}")
else:
    text = SKILL.read_text(encoding="utf-8")

    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    parts = text.split("---", 2)
    frontmatter = parts[1] if len(parts) >= 3 else ""

    for field in ("name:", "description:"):
        if field not in frontmatter:
            fail(f"Missing frontmatter field: {field[:-1]}")

    if "name: ugc-product-review" not in frontmatter:
        fail("Skill name must be 'ugc-product-review'")

    # Resolve every explicitly referenced Markdown file from the skill root.
    refs = sorted(set(re.findall(r"`((?:references|agents)/[^`]+\.(?:md|yaml))`", text)))
    for ref in refs:
        path = SKILL_DIR / ref
        if not path.exists():
            fail(f"Referenced file does not exist: {ref}")

    line_count = len(text.splitlines())
    if line_count > 220:
        fail("SKILL.md is too large; keep the router concise and move detail into references")
    elif line_count > 180:
        warn(f"SKILL.md is approaching the repository size guard ({line_count} lines)")


# Agent Plugins v1 package manifest
if not PLUGIN.exists():
    fail("Missing root plugin.json for Agent Plugins packaging")
else:
    try:
        plugin = json.loads(PLUGIN.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"plugin.json is invalid JSON: {exc}")
        plugin = {}

    allowed = {
        "$schema", "name", "version", "description", "author", "homepage",
        "repository", "license", "keywords", "extensions"
    }
    unknown = sorted(set(plugin) - allowed)
    if unknown:
        fail(f"plugin.json contains unsupported top-level fields: {', '.join(unknown)}")

    if plugin.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        fail("plugin.json must target the Agent Plugins 1.0.0 schema")

    name = plugin.get("name", "")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?", name):
        fail("plugin.json name violates Agent Plugins naming constraints")
    if "--" in name or ".." in name:
        fail("plugin.json name must not contain consecutive hyphens or periods")


# Optional OpenAI / Codex UI metadata
if not OPENAI.exists():
    warn("Missing agents/openai.yaml; Codex UI metadata will be unavailable")
else:
    openai_text = OPENAI.read_text(encoding="utf-8")
    for field in ("display_name:", "short_description:", "default_prompt:"):
        if field not in openai_text:
            fail(f"agents/openai.yaml missing interface field: {field[:-1]}")

    match = re.search(r'short_description:\s*["\']([^"\']+)["\']', openai_text)
    if match and not 25 <= len(match.group(1)) <= 64:
        fail("agents/openai.yaml short_description must be 25-64 characters")


required = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "SECURITY.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / "AGENTS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "docs" / "ARCHITECTURE.md",
    ROOT / "docs" / "COMPATIBILITY.md",
    SKILL_DIR / "references" / "core.md",
    SKILL_DIR / "references" / "creative-strategy.md",
    SKILL_DIR / "references" / "prompt-compiler.md",
]
for path in required:
    if not path.exists():
        fail(f"Missing required file: {path.relative_to(ROOT)}")


if warnings:
    print("Skill validation warnings:")
    for warning in warnings:
        print(f"- {warning}")

if errors:
    print("Skill validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Skill validation passed.")
