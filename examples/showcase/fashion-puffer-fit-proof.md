# Showcase #2: Navy quilted puffer jacket — fit-proof UGC

Status: **awaiting generation — recompiled for native 8-second Veo clips**

## At a glance

**Case ID:** `FASHION-PUFFER-002`

**Product/category:** Navy quilted puffer jacket / fashion

**Workflow/model:** Google Flow / Veo, using the tested practical constraint of **8 seconds per generated clip**

**Creative angle:** Buyer-doubt-led fit proof with product inspection, try-on, mirror proof, and a natural verdict

**Primary visual proof:** The jacket's real-world silhouette, puffiness, shoulder fit, length, and material behavior while handled and worn

**Current result:** The original 12–13 second concepts have been recompiled into a native **2 × 8-second production plan** before first generation. No generated output is claimed yet.

**QA:** Pending real generation

## Why this case was recompiled before generation

Showcase #1 established a practical production lesson for the tested Google Flow / Veo workflow: asking a single generation to carry a 12–13 second multi-state story creates unnecessary temporal pressure when the workflow returns 8-second clips.

Showcase #2 therefore does **not** begin by testing an overlong prompt and repairing it afterward. It applies the validated lesson up front:

- design natively for **2 × 8-second clips**;
- give each clip one dominant physical objective;
- repeat critical product and creator locks in each clip;
- define the cross-clip state explicitly;
- give clip 2 an **immutable opening state**;
- forbid regression to the pre-worn garment state;
- reserve stable screen time for the fit hero;
- use a hard cut rather than a generated transition.

The goal is not to copy the appliance case mechanically. The continuation-state rule is adapted to fashion: clip 2 must begin with the jacket **already fully worn**, rather than allowing the model to reconstruct the folded/held/partially worn state from clip 1.

## Evidence

Product/reference input: a navy quilted puffer jacket reference image supplied for this case. Generated-video evidence will be added only after a real generation run.

## Exact ask

```text
Create a realistic UGC fashion review for the navy quilted puffer jacket reference, optimized for the tested Google Flow / Veo workflow. Apply the lessons from the appliance showcase instead of forcing a 12–13 second story into one generation.
```

## Agent route

```text
core
+ creative-strategy
+ categories/fashion
+ prompt-compiler
+ model-adapters
```

`qa-and-repair` is not active yet because no real Showcase #2 output has been generated. It should be loaded only after V01 exists.

## Product/reference lock

Use the supplied product reference as the visual authority in every clip.

Preserve only visible or reliably supplied details:

- deep navy color;
- horizontal quilt geometry and panel spacing;
- material finish and believable puffiness;
- stand collar;
- centered front zipper;
- sleeves and cuffs;
- hem and jacket length;
- visible pockets when readable in the reference;
- overall proportions and silhouette.

Do not invent logos, labels, buttons, trims, extra pockets, extra zippers, removable parts, or technical features.

## Recommended concept — “Does it actually look like the photos?”

This remains the primary concept because it maps a common fashion buyer doubt directly to visible proof:

```text
BUYER DOUBT
→ PRODUCT / MATERIAL PROOF
→ TRY-ON
→ HARD CUT / TIME ADVANCE
→ ALREADY-WORN OPENING STATE
→ FIT HERO
→ DETAIL PROOF
→ NATURAL VERDICT
```

The production unit is now **two independent 8-second generations**, not one 13-second generation.

# V01 production plan — 2 × 8s

## Shared continuity lock

Apply this to both clips:

```text
Use the supplied navy quilted puffer jacket reference as the exact product authority.

Keep the exact same deep navy color, horizontal quilting geometry, panel spacing, material finish, puffiness, stand collar, centered front zipper, sleeves, cuffs, hem, visible pocket placement, jacket length, and overall proportions.

Keep the same creator identity, face, hair, complexion, body proportions, base outfit underneath the jacket, room, mirror, daylight direction, and casual smartphone UGC character across both clips.

Do not redesign the jacket between clips. Do not add or remove garment details. No logo invention, extra pockets, extra zippers, changing quilt layout, changing jacket length, changing color, or changing silhouette.

Natural home daylight. Vertical 9:16 smartphone footage. Slight human handheld imperfection or a simple static mirror-phone setup. No cinematic orbit, studio lighting, runway styling, slow motion, generated captions, or commercial end card.
```

## CLIP 1 — BUYER DOUBT → MATERIAL PROOF → TRY-ON START

**Dominant physical objective:** establish the real garment, then begin a believable try-on without also forcing the fit payoff into the same generation.

```text
TITLE
Navy Puffer Fit Review — V01 Clip 1 — Product Proof and Try-On

OBJECTIVE
Create one 8-second vertical 9:16 realistic smartphone UGC clip. The creator is casually checking whether the jacket will look as good in real life as it does in the product reference.

PRODUCT LOCK
Use the supplied navy quilted jacket reference as the exact authority. Preserve its deep navy color, horizontal quilt pattern, panel spacing, material finish, puffiness, stand collar, centered zipper, sleeves, cuffs, hem, visible pockets, length, and proportions. Do not invent garment details.

CREATOR / ENVIRONMENT
Use one creator in an ordinary bright bedroom or dressing area with a mirror nearby. Natural daylight, relaxed body language, normal base outfit, no commercial-model posing. Keep creator identity and base outfit stable for the continuation clip.

0:00–0:02 — BUYER-DOUBT HOOK
Begin with the creator holding the jacket naturally against or beside her torso so both the garment and its overall shape are readable.

She says in a casual, observational tone:
“I wanted to see if this actually looked like the pictures.”

0:02–0:04 — MATERIAL / SHAPE PROOF
Hard cut to a closer handheld view. She lightly compresses one quilted panel between her fingers, releases it, then lets the jacket hang naturally from one hand.

Show realistic fabric compression, recovery, gravity, and drape. Do not make the jacket inflate, float, stiffen, or change quilting.

No dialogue.

0:04–0:08 — TRY-ON START
Hard cut. She begins putting on the exact same jacket with one simple physically plausible sequence: first arm into one sleeve, then the second arm begins entering the other sleeve.

Do not require the clip to finish with a perfect styled pose. Prioritize believable shoulder, sleeve, cuff, hem, and fabric movement during dressing.

End during or just after the natural completion of the dressing action. Do not include the final fit verdict yet.

AUDIO
Quiet room tone, natural clothing rustle, and the opening spoken hook. No dramatic music.

PHYSICS / REALISM
Correct hand-to-fabric contact. Natural garment weight. Quilted panels compress where held. Sleeves bend with the arms. No cloth clipping into the body, duplicated limbs, deformed fingers, instant wardrobe transformation, or fabric morphing.

END-STATE CONTRACT
By the end of this clip, the try-on action has occurred. The next clip takes place moments later after the jacket is fully settled on the same creator.
```

## State handoff

Clip 1 establishes:

```text
same creator
+ same base outfit
+ same navy jacket
+ same room / mirror
+ try-on has occurred
```

Clip 2 must **not replay or reconstruct** the held, folded, or partially worn state. It begins after the dressing action is complete.

## CLIP 2 — IMMUTABLE WORN STATE → FIT HERO → NATURAL VERDICT

**Dominant physical objective:** prove how the jacket actually fits when worn.

```text
TITLE
Navy Puffer Fit Review — V01 Clip 2 — Already-Worn Fit Proof

OBJECTIVE
Create one 8-second vertical 9:16 realistic smartphone UGC continuation clip. The try-on shown in clip 1 has already finished before this clip begins. The only major goal is to give the viewer enough stable visual evidence to judge the jacket's real-world fit.

REFERENCE PRIORITY
1. The original supplied product reference is the authority for garment geometry, color, quilting, collar, zipper, pockets, material, length, and proportions.
2. Clip 1 is the continuity reference for creator identity, hair, complexion, body proportions, base outfit, room, mirror, daylight, and casual phone-camera character.
If clip 1 conflicts with the original garment reference, preserve the original garment reference.

IMMUTABLE OPENING STATE — CRITICAL
The dressing action has already fully completed before frame 1.

At frame 1:
- the exact same creator is already wearing the exact same navy quilted jacket;
- both arms are fully inside the correct sleeves;
- the jacket is naturally settled on the shoulders and torso;
- the collar, zipper, quilting, cuffs, hem, pockets, length, and silhouette already match the reference;
- the same base outfit remains underneath;
- the creator is already positioned at the same mirror / dressing area.

This worn state is immutable for the entire clip.

FORBIDDEN REGRESSIONS
Never return to a folded jacket.
Never show the jacket back in the creator's hands as an unworn object.
Never replay the dressing action.
Never show a sleeve empty and then suddenly occupied.
Never morph the jacket onto the creator.
Never change the quilt pattern, color, length, collar, zipper, pockets, puffiness, or body scale during a cut or mirror view.

0:00–0:04 — FIT HERO
Start immediately on a three-quarter or near-full mirror view with the jacket already fully worn.

Hold the framing stable enough for the viewer to inspect the front fit, shoulder volume, torso silhouette, puffiness, and jacket length.

The creator makes only one small natural turn from front toward a slight side angle. No runway pose, spin, or fast camera movement.

No dialogue during the first 2 seconds of the hero proof.

0:04–0:06 — DETAIL PROOF
Without changing garment state, she lightly adjusts the existing collar or smooths the hem once. Use a simple hand action that demonstrates material structure without hiding the jacket.

Keep mirror geometry coherent. The reflection must match the creator's body, movement, and exact jacket state.

0:06–0:08 — NATURAL VERDICT
Keep the jacket clearly visible. She looks at the fit rather than presenting directly to the camera and says with a restrained reaction:
“Yeah... this is pretty much exactly what I wanted.”

Finish on the worn fit. No thumbs-up, pointing, broad grin, product-to-face pose, or call-to-action.

AUDIO
Natural room ambience, subtle fabric rustle, natural voice. No dramatic music.

PHYSICS / PRODUCT FIDELITY
Natural textile weight, compression, drape, sleeve bending, shoulder contact, and hem movement. No cloth-body intersections, floating fabric, mirror mismatch, hand deformation, garment morphing, or sudden change in puffiness.

PASS CONDITION
The clip only passes if the jacket is already fully and correctly worn from the first frame and stays in that exact product state while the fit proof remains readable.
```

## Edit assembly

Join the two generated outputs with a simple hard cut:

```text
Clip 1 buyer doubt
→ material proof
→ try-on begins / completes
→ hard cut forward a few moments
→ Clip 2 already-worn fit hero
→ detail proof
→ restrained verdict
```

The cut intentionally skips unimportant dressing time. It should read as a normal creator edit, not as missing continuity.

Do not ask Veo to generate a transition effect between clips. Do not add a morph, whip transition, flash, or outfit-change effect.

A minimal audio cut is acceptable. Captions, if needed for publishing, should be added in post rather than generated in-scene.

## Why this is safer than the original 13-second prompt

The previous prompt asked one generation to handle:

```text
hook
+ product inspection
+ full dressing interaction
+ mirror transition
+ fit hero
+ detail proof
+ verdict
```

The recompiled version separates the two fragile responsibilities:

```text
CLIP 1 = garment handling + dressing physics
CLIP 2 = already-worn garment continuity + fit proof
```

This reduces simultaneous demands on hands, fabric simulation, mirror geometry, creator continuity, timing, and dialogue.

## V01 pass criteria

The first generation should be considered successful only if:

- both clips preserve the same jacket geometry, color, quilting, material character, and scale;
- the creator identity and base outfit remain coherent across clips;
- clip 1 shows physically plausible garment handling and dressing;
- clip 2 begins with the jacket already fully worn, with no regression to an earlier state;
- the mirror does not create a duplicate, mismatched, or redesigned jacket;
- the fit hero receives at least about 2 seconds of stable readable screen time before dialogue competes with it;
- fabric weight, puffiness, compression, sleeve movement, and hem movement remain plausible;
- the creator reaction stays observational rather than commercial;
- the hard cut feels like a normal UGC edit.

## Alternative 8-second concepts

These are intentionally **standalone 8-second tests**, not compressed 12-second stories. They are useful if the primary 2-clip concept succeeds and the showcase needs broader fashion coverage.

### Alternative A — Material proof only

```text
Create one 8-second vertical realistic smartphone UGC clip using the exact navy quilted jacket reference.

0:00–0:02 — close material hook: creator compresses one quilted panel and says, “Okay, this feels way nicer than I expected.”
0:02–0:05 — inspect zipper, collar, stitching, and fabric with simple hand movements.
0:05–0:08 — let the jacket hang naturally and lightly flex one sleeve to show weight and structure.

Do not include a try-on or mirror shot. This clip has one job: prove material behavior and construction visually.

Preserve exact color, quilt geometry, collar, zipper, cuffs, hem, pockets, proportions, and material. Natural daylight, phone-camera realism, ordinary room ambience, realistic hands and gravity. No product morphing, extra features, captions, cinematic camera movement, or commercial posing.
```

### Alternative B — Already-worn skeptical fit test

```text
Create one 8-second vertical realistic smartphone UGC mirror-review clip using the exact navy quilted jacket reference.

The jacket is already fully worn from frame 1. This state is immutable.

0:00–0:02 — creator looks at the side silhouette and says, “I thought this was gonna look really bulky.”
0:02–0:06 — stable fit proof: one small front-to-side turn, showing shoulder volume, torso silhouette, and length.
0:06–0:08 — creator lightly touches the collar and says, “Wait... this is actually really flattering.”

No dressing sequence. No jacket-in-hand state. No transition effect. Preserve exact garment geometry and mirror continuity. Natural restrained performance, no thumbs-up or runway pose.
```

### Alternative C — Everyday routine fit proof

```text
Create one 8-second vertical realistic smartphone UGC lifestyle clip with the exact navy quilted jacket already fully worn from frame 1.

0:00–0:02 — creator checks the fit in a hallway mirror and says, “Okay... this outfit is actually working.”
0:02–0:05 — she adjusts the existing collar or zipper once while the silhouette remains readable.
0:05–0:08 — she picks up keys and takes one or two natural steps toward the door while the jacket moves realistically with her body.

One physical objective: demonstrate the jacket during normal worn movement. No dressing sequence, no product reset, no cinematic tracking, no commercial end pose, no invented garment details.
```

## What this case is intended to test

Showcase #2 now tests whether the lessons from the completed appliance lifecycle transfer to a different physical domain:

1. whether native clip-duration planning improves generation reliability before a failure occurs;
2. whether explicit continuation contracts prevent fashion-state regression;
3. whether separating dressing physics from mirror-fit proof improves garment fidelity;
4. whether a stable hero hold gives enough time to judge silhouette and fit;
5. whether garment and creator continuity survive a hard-cut multi-clip workflow;
6. whether the skill can adapt a reusable production rule without blindly copying category-specific appliance logic.

## Expected failure classes to watch

Do not assume these will occur; use them only if visible in the real output:

```text
PRODUCT_MORPH
COLOR_DRIFT
SCALE_DRIFT
STATE_DISCONTINUITY
IDENTITY_DRIFT
HAND_DEFORMATION
GRIP_ERROR
FABRIC_PHYSICS
BODY_MECHANICS_ERROR
HERO_MOMENT_TOO_FAST
TOO_CINEMATIC
TOO_COMMERCIAL
PACING_ERROR
```

For this fashion case, also record plain-language observations for mirror mismatch, cloth-body clipping, changing quilt geometry, or implausible puffiness even when a dedicated taxonomy tag does not exist.

## Next step

Generate **V01 Clip 1** and **V01 Clip 2** separately using the same original jacket reference.

For Clip 2, use Clip 1 only as a creator/environment continuity reference; the original product image remains the higher-priority garment authority.

After both real outputs exist:

```text
GENERATE V01 CLIP 1 + CLIP 2
→ REVIEW EACH CLIP
→ REVIEW CROSS-CLIP CONTINUITY
→ SCORE QA
→ CLASSIFY ROOT CAUSE
→ REPAIR ONLY THE FAILED CLIP / FAILED CONTRACT
→ REGENERATE
```

Do not rewrite both clips automatically if only one fails. Preserve the successful clip and make the smallest targeted repair, following the same controlled-repair principle validated by Showcase #1.
