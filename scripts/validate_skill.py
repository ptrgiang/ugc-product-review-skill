#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ugc-product-review" / "SKILL.md"

errors = []

if not SKILL.exists():
    errors.append(f"Missing canonical skill: {SKILL.relative_to(ROOT)}")
else:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    frontmatter = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    for field in ("name:", "description:"):
        if field not in frontmatter:
            errors.append(f"Missing frontmatter field: {field[:-1]}")

    if "name: ugc-product-review" not in frontmatter:
        errors.append("Skill name must be 'ugc-product-review'")

    refs = sorted(set(re.findall(r"`(references/[^`]+\.md)`", text)))
    for ref in refs:
        path = SKILL.parent / ref
        if not path.exists():
            errors.append(f"Referenced file does not exist: {ref}")

    if len(text.splitlines()) > 220:
        errors.append("SKILL.md is too large; keep the router concise and move detail into references")

required = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "CONTRIBUTING.md",
    SKILL.parent / "references" / "core.md",
    SKILL.parent / "references" / "creative-strategy.md",
    SKILL.parent / "references" / "prompt-compiler.md",
]
for path in required:
    if not path.exists():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")

if errors:
    print("Skill validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Skill validation passed.")
