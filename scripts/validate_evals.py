#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ugc-product-review"
FIXTURES_DIR = ROOT / "evals" / "fixtures"

REQUIRED_KEYS = {
    "id",
    "category",
    "request",
    "product_context",
    "expected_modules",
    "forbidden_modules",
    "expected_behavior",
    "critical_constraints",
    "failure_conditions",
}

CATEGORY_ROUTE = {
    "appliances": "references/categories/appliances.md",
    "fashion": "references/categories/fashion.md",
    "beauty": "references/categories/beauty.md",
    "home-utility": "references/categories/home-utility.md",
    "electronics": "references/categories/electronics.md",
    "food-beverage": "references/categories/food-beverage.md",
    "tools-diy": "references/categories/tools-diy.md",
    "pet": "references/categories/pet.md",
}

errors = []
fixtures = []

if not FIXTURES_DIR.exists():
    errors.append("Missing evals/fixtures directory")
else:
    for path in sorted(FIXTURES_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue
        fixtures.append((path, data))

if len(fixtures) < 7:
    errors.append(f"Expected at least 7 baseline fixtures, found {len(fixtures)}")

seen_ids = set()
for path, data in fixtures:
    missing = REQUIRED_KEYS - data.keys()
    if missing:
        errors.append(f"{path.name}: missing keys: {', '.join(sorted(missing))}")
        continue

    fixture_id = data["id"]
    if fixture_id in seen_ids:
        errors.append(f"{path.name}: duplicate id: {fixture_id}")
    seen_ids.add(fixture_id)

    if path.stem != fixture_id:
        errors.append(f"{path.name}: filename must match id '{fixture_id}.json'")

    category = data["category"]
    expected = data["expected_modules"]
    forbidden = data["forbidden_modules"]

    if not isinstance(expected, list) or not expected:
        errors.append(f"{path.name}: expected_modules must be a non-empty list")
        continue
    if not isinstance(forbidden, list):
        errors.append(f"{path.name}: forbidden_modules must be a list")
        continue

    overlap = sorted(set(expected) & set(forbidden))
    if overlap:
        errors.append(f"{path.name}: modules cannot be both expected and forbidden: {overlap}")

    if "references/core.md" not in expected:
        errors.append(f"{path.name}: every baseline fixture must expect references/core.md")

    routed_category = CATEGORY_ROUTE.get(category)
    if routed_category and routed_category not in expected:
        errors.append(f"{path.name}: category '{category}' should expect {routed_category}")

    for module in set(expected) | set(forbidden):
        if not module.startswith("references/") or not module.endswith(".md"):
            errors.append(f"{path.name}: invalid module path: {module}")
            continue
        module_path = SKILL_DIR / module
        if not module_path.exists():
            errors.append(f"{path.name}: module does not exist: {module}")

    for key in ("expected_behavior", "critical_constraints", "failure_conditions"):
        value = data[key]
        if not isinstance(value, list) or len(value) < 2 or not all(isinstance(item, str) and item.strip() for item in value):
            errors.append(f"{path.name}: {key} must contain at least two non-empty strings")

if errors:
    print("Eval validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Eval validation passed: {len(fixtures)} fixtures")
for path, data in fixtures:
    print(f"- {data['id']} ({data['category']})")
