# Adoption Checklist

Use this checklist when preparing the skill for another coding agent or team.

## Install

- [ ] Install with `npx skills@latest add ptrgiang/ugc-product-review-skill --skill ugc-product-review` or the client's native skill installer.
- [ ] Confirm the client discovers `ugc-product-review` from frontmatter metadata.
- [ ] Confirm the client can resolve relative files under `references/`.
- [ ] Confirm only relevant modules are loaded during a normal one-product request.

## Smoke prompts

### Activation

```text
Create a realistic UGC review video for this product.
```

Expected: skill activates and chooses an angle without unnecessary questions.

### Campaign routing

```text
Create 5 genuinely different UGC review concepts for this product.
```

Expected: campaign logic loads and concepts differ in hook/proof/hero moment.

### Repair routing

```text
The generated video changes the product shape and the hands look wrong. Repair the prompt.
```

Expected: QA/repair logic loads; campaign/performance modules should not be needed.

## Production checks

- [ ] Product facts are not invented.
- [ ] Product and creator locks are present when references exist.
- [ ] First frame and hero moment are clear.
- [ ] Product interactions are physically plausible.
- [ ] Dialogue fits duration.
- [ ] Category-specific negative constraints are targeted, not generic.
- [ ] The output feels like UGC unless a polished ad is explicitly requested.

## Report compatibility

When contributing a compatibility result, include:

- client and version
- installation method
- platform/OS
- activation prompt
- whether progressive reference loading worked
- any caveat or unsupported field
