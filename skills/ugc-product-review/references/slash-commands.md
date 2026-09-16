# Slash-command preset router

Load this file only when the user explicitly types a recognized slash-style preset (for example `/productshot`, `/storyboard`, `/hookframe`) or asks to browse/use the preset library.

These are **textual intent presets**, not platform-native commands. Treat them as compact creative directives that modify the requested deliverable.

## Core rule

Slash presets are modifiers, not replacements for the skill's normal reasoning.

Keep this precedence:

1. explicit user instructions and supplied references
2. factual / safety / claim constraints
3. product and creator locks from `core.md`
4. the selected task route and category rules
5. the slash preset
6. default creative choices

A preset must never override product identity, creator identity, physical plausibility, or claim/compliance constraints.

## Input pattern

Interpret:

```text
/<command> + subject + context + mood + output goal
```

Example:

```text
/productshot insulated bottle, white studio background, premium but realistic
```

Only the slash token is fixed. Everything after it is user context and should be preserved unless it conflicts with a higher-priority constraint.

## Progressive-disclosure routing

After recognizing the command, open only the matching group file:

- Product / e-commerce → `slash-commands/product-ecommerce.md`
- Fashion / model → `slash-commands/fashion-model.md`
- Portrait / people / character → `slash-commands/people-character.md`
- Brand / advertising / marketing → `slash-commands/brand-marketing.md`
- YouTube / TikTok / social → `slash-commands/social-content.md`
- Storyboard / video / cinema → `slash-commands/video-cinema.md`
- Horror / supernatural → `slash-commands/horror-supernatural.md`
- Documents / presentation / infographic → `slash-commands/document-visuals.md`

Do not open all eight files just because a slash preset is present.

## Command index

### Product / e-commerce
`/productshot` `/packshot` `/ecommerce` `/whitebg` `/transparentcutout` `/lifestyleproduct` `/premiumproduct` `/macrodetail` `/flatlay` `/productcomparison`

### Fashion / model
`/modellook` `/lookbook` `/streetstyle` `/runway` `/fashioneditorial` `/catalogmodel` `/outfitfocus` `/luxuryfashion` `/minimalfashion` `/seasoncampaign`

### Portrait / people / character
`/portrait` `/headshot` `/cinematicportrait` `/reallifeshot` `/beautyshot` `/characterdesign` `/characterref` `/expressionboard` `/costumetest` `/identitylock`

### Brand / advertising / marketing
`/adcreative` `/commercial` `/campaignvisual` `/brandposter` `/socialad` `/promobanner` `/launchposter` `/offercreative` `/billboardstyle` `/premiumad`

### YouTube / TikTok / social
`/thumbnail` `/viralthumbnail` `/youtubecover` `/tiktokcover` `/socialpost` `/carouselpost` `/quotegraphic` `/channelart` `/episodetitlecard` `/hookframe`

### Storyboard / video / cinema
`/storyboard` `/shotlist` `/cinematicframe` `/filmscene` `/establishingshot` `/mediumshot` `/closeupshot` `/actionframe` `/behindthescenes` `/continuityframe`

### Horror / supernatural
`/horror` `/horrorposter` `/ghostscene` `/darkcinematic` `/folkhorror` `/hauntedhouse` `/ritualscene` `/creepythumbnail` `/moodhorror` `/supernatural`

### Documents / presentation / infographic
`/specsheet` `/infographic` `/comparisonchart` `/timeline` `/processdiagram` `/flowchart` `/mindmap` `/presentationslide` `/factcard` `/trainingvisual`

## Combination behavior

Prefer one primary preset per deliverable. If the user combines compatible presets, use the first as the output type and later presets as modifiers.

Example:

```text
/productshot /premiumproduct espresso machine
```

Interpret as a product-shot deliverable with a premium-product treatment.

If presets conflict, preserve the user's explicit wording and choose the interpretation that best protects product fidelity and output clarity. Ask a clarification only when the conflict materially changes the requested result.

## UGC-skill boundary

Many presets are useful as UGC pre-production or support assets, especially:

`/productshot`, `/lifestyleproduct`, `/macrodetail`, `/modellook`, `/catalogmodel`, `/reallifeshot`, `/characterref`, `/identitylock`, `/adcreative`, `/tiktokcover`, `/hookframe`, `/storyboard`, `/shotlist`, and `/continuityframe`.

Other presets may be outside a normal product-review workflow. Honor them only when explicitly invoked; do not let them silently broaden a standard UGC request.

## Output behavior

A slash preset should result in a concrete output specification or generation-ready prompt for that preset's deliverable. Do not merely explain what the command means unless the user asks for documentation.

When the preset is used inside a larger UGC-video request, integrate it into the relevant section of the existing output instead of producing a disconnected artifact.
