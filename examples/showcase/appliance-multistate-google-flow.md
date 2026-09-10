# Showcase candidate: Appliance multi-state — Google Flow

Status: **real generation reviewed; V02 ready for regeneration**

This case stress-tests the failure modes most relevant to appliance UGC: product geometry drift, control-panel drift, lid/contact physics, hand quality, state continuity, hero-moment timing, and the practical effect of model clip-duration constraints.

## Case ID

`FLOW-APPLIANCE-001`

## Product reference

The real test used a white countertop food processor/chopper with:

- one clear removable processing bowl
- one clear locking lid
- a right-side clear handle
- a central white spindle
- two circular controls on the lower front body
- a visible chopped-food transformation

The reference image is the authority for geometry, proportions, color, materials, control placement, handle placement, lid design, bowl scale, and visible branding. No prompt revision may invent extra controls, labels, modes, capacities, wattage, or proprietary features.

## Creative angle

**Skeptical → impressed fast demo**

Buyer doubt: does the appliance produce a visibly useful result without making the workflow feel complicated?

Primary visual proof: the same bowl changes from visibly separate ingredients to a clearly processed salsa/chopped result.

## Original target structure

The first design assumed an approximately 12-second continuous creator-style video:

- **0:00–0:02 — result-first hook**
- **0:02–0:05 — setup**
- **0:05–0:07 — start**
- **0:07–0:10 — hero reveal**
- **0:10–0:12 — restrained verdict**

## V01 — original Google Flow / Veo-style prompt

```text
Create a realistic 12-second vertical 9:16 smartphone UGC product-review video in an ordinary bright home kitchen.

Use one consistent countertop kitchen appliance for the entire video: the exact same body shape, proportions, color, material, removable container, locking lid, logo placement if present, and visible control-panel layout in every shot. Do not redesign or relocate any controls. Do not add buttons or labels that are not visible in the product reference.

The creator is casual and natural, filmed like a real social-media review rather than a polished commercial. Natural window light, slight handheld phone movement, small autofocus imperfections, hard cuts, no cinematic camera orbit, no studio lighting, no on-screen captions or logo card.

0:00–0:02 — RESULT-FIRST HOOK
Start with the finished removable container beside the appliance, already showing a clearly transformed food or liquid result. Keep both the product and result readable. The creator says, with restrained surprise: “Okay… that actually worked.”

0:02–0:05 — SETUP
Cut back to the same appliance before processing. The same removable container is loaded and seated correctly in the same product. One hand stabilizes the appliance or container while the other closes and locks the lid with one simple continuous action. The lid keeps the same hinge/latch orientation and geometry. No crossed hands and no complex finger choreography.

0:05–0:07 — START
Show the same unchanged control panel from a stable medium-close angle. The creator presses one existing visible control once. Do not invent a named mode or feature. The appliance responds with believable mechanical or motor sound and begins operating while remaining supported on the counter.

0:07–0:10 — HERO REVEAL
Hard cut to the finished state after processing. The appliance, container, lid, and controls are still identical. One hand stabilizes the product while the other unlocks and opens the lid using one simple motion. Reveal the visibly transformed contents in the same removable container. Hold the readable result for about 1.5–2 seconds. During the hero reveal, use almost no camera movement and no overlapping dialogue.

0:10–0:12 — VERDICT
Keep the transformed result visible. The creator gives a small, believable impressed reaction and says: “Yeah, I’d use this again.”

Audio should prioritize natural kitchen ambience, lid/latch contact, one control press, believable appliance operation, and the creator’s voice. No dramatic music is necessary.

Physical constraints: realistic product weight and support, stable container position, unchanged lid orientation, unchanged button positions, believable contents level, no floating parts, no product morphing, no changing scale, no impossible motor movement, no deformed hands.

If maintaining all states in one generation causes product drift, preserve this exact creative sequence but generate the setup/start and reveal/verdict as separate short clips using the same product reference and continuity description.
```

## Real-generation evidence — V01

Generation date: **2026-09-10**

Workflow: **Google Flow / Veo**

Observed practical constraint: **8 seconds per generated video in the tested flow**.

The generation therefore produced two 8-second outputs instead of one 12-second continuous output:

- `v01-clip-1`: setup / product interaction / processing-oriented footage
- `v01-clip-2`: processed salsa / reveal / verdict-oriented footage

The original product reference and both generated MP4 files were retained from the test session. Full-resolution media should be attached to this showcase using lightweight Git storage while the evidence set is small; if the repository grows substantially, move full videos to Git LFS or release assets and keep stable links here.

### Preliminary visual QA

| Dimension | Score | Observation |
| --- | ---: | --- |
| Product fidelity | 2 / 2 | White body, clear bowl, right-side handle, central spindle, and two-control layout remain recognizably stable. |
| Creator continuity | 2 / 2 | No major creator discontinuity was observed across the useful footage. |
| Physical plausibility | 2 / 2 | Core lid/bowl/product interactions are generally believable. |
| Hand quality | 2 / 2 | Hands are usable and do not dominate the failure profile. |
| State continuity | 1 / 2 | Splitting generation reduces overload but makes cross-clip state handoff dependent on repeated locks and edit assembly. |
| Hero clarity | 1 / 2 | The salsa result is present, but the before/after transformation is not visually strong enough to carry the payoff by itself. |
| UGC realism | 1 / 2 | Overall creator-style framing works, but the final thumbs-up reads as a generic ad convention. |
| Prompt adherence | 2 / 2 | The core appliance demo, interaction, and result sequence were substantially followed. |
| **Total** | **13 / 16** | Good enough to validate the concept; not yet a showcase-quality final creative. |

### What worked

- Product geometry stayed substantially more stable than expected for a multi-state appliance case.
- The visible control layout did not become the main failure.
- Splitting difficult interactions into short clips is operationally more reliable than forcing the entire state graph into one long generation.
- The ordinary kitchen setting and smartphone-style framing support the intended UGC language.

### What failed or weakened the proof

- The tested workflow's 8-second generation limit makes the original 12-second single-video design impractical.
- The transformation contrast is too modest: processed salsa is visible, but the hero result does not immediately read as a dramatic enough `before → after` proof.
- The final thumbs-up is generic and makes the ending feel more like synthetic ad shorthand than observed creator behavior.
- Cross-clip continuity becomes an explicit production responsibility once the sequence is split.

### Error tags

- `HERO_MOMENT_TOO_FAST`
- `TOO_COMMERCIAL`
- `PACING_ERROR`

The modest transformation contrast is recorded as a case-specific observation rather than inventing a new taxonomy tag.

## Root-cause diagnosis

The primary issue is not weak product locking. V01 attempted to allocate five narrative states inside a duration the tested Flow workflow does not provide as one generation. Even after automatic splitting, the original timing logic still behaves like a 12-second story compressed into short outputs.

That creates two downstream problems:

1. too much narrative responsibility is placed on each clip, reducing dedicated hero-proof time;
2. the verdict becomes a fast symbolic gesture instead of a natural continuation of the product result.

## Repair strategy

V02 changes only the production decisions responsible for the observed weakness:

- compile the concept natively as **2 × 8-second clips**;
- give each clip **one physical objective**;
- repeat the critical product/reference lock in both clips;
- define an explicit state handoff between clips;
- make the ingredient state and processed state visually different enough to read instantly;
- reserve approximately 2 seconds in clip 2 for a stable result shot;
- replace the thumbs-up with a small result-focused action and restrained spoken reaction;
- keep the kitchen, product geometry, controls, bowl, handle, creator styling, and UGC camera language unchanged.

## V02 — 2 × 8s split-clip production plan

### Shared continuity lock

Use the supplied product reference as the visual authority in both clips. Preserve exactly the same white appliance body, proportions, clear bowl, clear locking lid, right-side handle, central white spindle, two circular front controls, logo placement if visible, countertop scale, creator, wardrobe, bright ordinary home kitchen, daylight direction, and smartphone UGC camera character.

Do not redesign the product between clips. Do not add controls, labels, displays, accessories, or modes. Keep camera height and general product scale similar enough that the clips can be hard-cut together naturally.

### CLIP 1 — SETUP → START

```text
Create an 8-second vertical 9:16 realistic smartphone UGC clip in the same bright ordinary home kitchen as the supplied reference.

Use the supplied food-processor reference as the exact product authority. Keep the identical white body, clear processing bowl, right-side clear handle, clear lid, central white spindle, two circular front controls, proportions, materials, scale, and visible logo placement. Do not invent or move any control.

0:00–0:02 — INGREDIENT PROOF
Begin close enough to clearly read the bowl contents: visibly separate chunks of tomato, red onion, cilantro/green herbs, and other salsa ingredients. The pieces should look intentionally coarse and unprocessed. Keep the appliance itself readable in frame.

0:02–0:05 — CLOSE AND SECURE
The creator uses one simple physically plausible interaction: one hand stabilizes the bowl/product while the other closes and secures the existing clear lid. Preserve the real lid geometry and right-side handle orientation. No crossed hands, no finger choreography, no floating parts.

0:05–0:08 — START
Use a stable medium-close view of the unchanged front controls. The creator presses one existing visible circular control once. The appliance begins believable operation while fully supported on the countertop. Let natural motor sound become the audio focus. End while the product is operating; do not reveal the final salsa yet.

Natural window light, slight handheld phone movement, minor autofocus/exposure behavior, ordinary kitchen ambience. No cinematic orbit, no studio lighting, no captions, no logo card, no exaggerated facial reaction.
```

### State handoff

At the end of clip 1:

```text
same appliance + same bowl + same lid + same handle orientation + same kitchen + processing underway
```

At the start of clip 2, preserve those locks but jump forward causally to processing completed.

### CLIP 2 — HERO RESULT → NATURAL VERDICT

```text
Create an 8-second vertical 9:16 realistic smartphone UGC clip that continues the same food-processor review in the same kitchen.

Use the same supplied product reference as the exact authority. The white body, clear bowl, right-side handle, clear lid, central spindle, two circular front controls, logo placement, proportions, materials, scale, creator, wardrobe, counter position, and daylight must match the first clip. Do not add or redesign anything.

The food state is now clearly processed: instead of large separate tomato/onion/herb chunks, the bowl contains a visibly finer, evenly chopped fresh salsa mixture. Keep it believable for a food processor; do not turn it into an impossible smooth liquid or make the bowl refill itself.

0:00–0:03 — OPEN
The appliance is stopped and fully supported. One hand stabilizes the bowl/product while the other releases and opens the real lid in one simple motion. Preserve lid and handle geometry. Natural latch/contact sound is audible.

0:03–0:06 — HERO RESULT
Hold a stable medium-close view of the opened bowl for about 2 seconds with almost no camera movement. Make the finer salsa texture immediately readable. The product body and result remain visible together. No dialogue over the first part of the reveal.

0:06–0:08 — NATURAL VERDICT
Instead of a thumbs-up or presenter pose, the creator keeps attention on the food: lightly tilts the bowl toward the phone or lifts a small spoonful/chip-sized taste sample without hiding the appliance. With a small restrained reaction, say: “Okay, that came out way better than I expected.”

Keep the delivery observational, not salesy. No broad grin, no pointing at the product, no product beside the face, no commercial end pose. Finish as if the creator is about to keep using or tasting the result.

Natural kitchen ambience and product-contact sounds. No dramatic music, captions, logo card, cinematic camera move, floating parts, changing product scale, control drift, lid morphing, impossible food physics, or deformed hands.
```

## Edit assembly

Join the two outputs with a simple hard cut.

Recommended final sequence:

```text
Clip 1 ingredient proof
→ lid interaction
→ control press / motor begins
→ hard cut
→ Clip 2 lid opens
→ stable processed-salsa hero
→ natural result-focused verdict
```

Do not add an animated transition. A short motor-sound bridge across the cut is acceptable if it makes the time jump feel natural. Captions, if required for publishing, should be added in post rather than generated inside the video.

## V02 pass criteria

V02 should improve the case only if:

- both clips preserve the exact reference product geometry and controls;
- coarse ingredients in clip 1 and finer salsa in clip 2 are instantly distinguishable;
- clip 2 gives the result approximately 2 seconds of stable readable screen time;
- lid and hand interactions remain physically plausible;
- no generic thumbs-up or presenter end pose appears;
- the hard-cut assembly feels like one creator session despite separate generations;
- the resulting edit still feels like a casual review rather than a polished commercial.

## Next step

Generate both V02 clips using the same product reference. Then compare V01 and V02 specifically on hero clarity, UGC authenticity, product fidelity, and cross-clip continuity. Do not broaden the prompt again unless the new output exposes a new root cause.
