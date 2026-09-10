---
name: ugc-product-review
description: Create, diversify, evaluate, and repair realistic UGC product-review video concepts and generation prompts from product references, creator references, product details, campaign goals, or generated video results. Use for TikTok, Reels, Shorts, affiliate UGC, organic reviews, paid UGC concepts, batch campaigns, prompt debugging, product-consistency repair, and performance-driven creative iteration.
---

# UGC Product Review

Create believable short-form product-review videos that feel observed rather than staged.

Optimize for:

- visual proof over marketing claims
- product fidelity over cinematic complexity
- physical plausibility over spectacle
- human imperfection over commercial polish
- focused context over loading every available reference

## Progressive disclosure

Do not load all reference files.

Always read `references/core.md`, then read only the smallest additional set that materially changes the answer.

### One product -> ideas or one review prompt

Read:

- `references/core.md`
- `references/creative-strategy.md`
- one relevant category file from `references/categories/`
- `references/prompt-compiler.md`

Read `references/model-adapters.md` only when a target video model is specified.

Read `references/commerce-and-claims.md` only when affiliate/paid UGC, factual claims, testimonials, health/wellness, or other claim-sensitive content matters.

### Batch or campaign

Read:

- `references/core.md`
- `references/creative-strategy.md`
- one relevant category file
- `references/campaign-engine.md`

Read `references/prompt-compiler.md` only when full generation prompts are requested.

### Generated video or frames need review

Read:

- `references/core.md`
- `references/qa-and-repair.md`

Add one category file only when product-specific physics or construction matters.

### Existing prompt needs repair

Read:

- `references/core.md`
- `references/qa-and-repair.md`
- `references/prompt-compiler.md`

### Performance metrics are supplied

Read:

- `references/core.md`
- `references/performance-learning.md`
- `references/campaign-engine.md`

Do not load prompt-generation references unless new prompts are also requested.

## Category routing

Choose one primary category unless the product genuinely spans categories:

- Appliances / kitchen machines: `references/categories/appliances.md`
- Fashion / footwear / bags: `references/categories/fashion.md`
- Beauty / skincare / personal care: `references/categories/beauty.md`
- Cleaning / organization / home utility: `references/categories/home-utility.md`
- Electronics / gadgets: `references/categories/electronics.md`
- Food / beverage: `references/categories/food-beverage.md`
- Tools / DIY: `references/categories/tools-diy.md`
- Pet products: `references/categories/pet.md`

If no category fits, stay conservative instead of importing multiple unrelated files.

## Default behavior

When the user gives a product or reference image and asks for a review video:

1. Identify product type and confidence.
2. Identify the strongest visible proof.
3. Identify the likely buyer motivation or doubt.
4. Choose the best review angle autonomously.
5. Design the first frame, hook, hero moment, and shot graph.
6. Produce one production-ready prompt.
7. Suggest two or three genuinely different alternative angles.

Do not ask configuration questions that are not necessary.

If the product's actual function is unclear and the chosen action would require guessing, ask one focused clarification.

## Default output

Unless the user requests another format:

### Creative diagnosis
Briefly state product type, strongest proof, and chosen angle.

### Recommended concept
State the hook, emotional arc, and hero moment.

### Production prompt
Return the prompt in a directly usable form.

### Alternatives
Suggest two or three non-duplicate angles.

## Quality gate

Before finalizing, verify:

- the product or result appears within the first two seconds when appropriate
- the strongest product value is demonstrated visually
- every shot has a narrative or proof function
- product and creator references remain consistent
- physical interactions are plausible
- dialogue fits the available time
- the hero moment has enough screen time
- the prompt is not overloaded
- the output looks like UGC rather than a polished commercial unless the user explicitly wants an ad

The best prompt is not the longest prompt. Use the smallest set of precise instructions that maximizes generation reliability.
