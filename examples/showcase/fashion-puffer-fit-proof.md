# Showcase #2: Navy quilted puffer jacket — fit-proof UGC

Status: **awaiting generation**

## At a glance

**Case ID:** `FASHION-PUFFER-002`

**Product/category:** Navy quilted puffer jacket / fashion

**Workflow/model:** Model-agnostic prompt set; real-generation workflow not recorded yet

**Creative angle:** Buyer-doubt-led fit proof with material inspection, try-on, mirror proof, and natural verdict

**Primary visual proof:** The jacket's real-world silhouette, puffiness, shoulder fit, length, and material behavior while handled and worn

**Current result:** Four generation-ready concepts prepared; Prompt 3 is the recommended primary concept. No generated output is claimed yet.

**QA:** Pending real generation

## Evidence

Product/reference input: a navy quilted puffer jacket image supplied for this case. The binary reference is not committed in this prompt-only update. Generated-video evidence will be added only after a real generation run.

## Exact ask

```text
Create prompts for Showcase #2 using the navy quilted puffer jacket reference. The concepts should demonstrate how the skill handles a fashion/wearable product with realistic product locking, material behavior, try-on, fit proof, mirror continuity, and natural UGC performance.
```

## Agent route

```text
core
+ creative-strategy
+ categories/fashion
+ prompt-compiler
```

No model adapter is required yet because no target generation model was specified. QA/repair will be loaded after real generated output exists.

## Product/reference lock

Keep the jacket consistent with the supplied reference in every shot. Preserve only visually supported details: navy color, quilting geometry, visible material finish, collar, front zipper, sleeves, cuffs, hem, pockets when visible, proportions, and overall silhouette. Do not invent logos, labels, fasteners, pockets, trims, or other product features.

## Recommended concept — Prompt 3: “Does it actually look like the photos?”

This is the primary concept because the structure directly connects a common buyer doubt to visible evidence:

```text
BUYER DOUBT → PRODUCT VIEW → TRY-ON → FIT HERO → DETAIL PROOF → NATURAL VERDICT
```

### Production prompt

```text
Create a 13-second realistic vertical smartphone UGC product-review video using the exact navy quilted puffer jacket from the supplied reference image.

CREATIVE OBJECTIVE
Answer the buyer question:
“Does the jacket actually look good when worn in real life?”

The video should prioritize visible proof of real-world fit over verbal claims.

PRODUCT LOCK
Preserve exactly:
navy color
quilt pattern
panel dimensions
material appearance
collar
zipper
pockets
sleeves
cuffs
hem
length
overall silhouette

0:00–0:02 — QUESTION HOOK
The creator holds the jacket next to her body before wearing it.

She says:
“I wanted to see if this actually looked like the pictures.”

0:02–0:04 — PRODUCT VIEW
Hard cut.
Close handheld view of the jacket hanging naturally from her hand.
Show the front, quilting, collar, and overall shape.

0:04–0:07 — PUTTING IT ON
Hard cut.
Show a realistic partial try-on sequence.
One arm enters a sleeve, then the other.
The fabric reacts naturally to pulling and contact.

0:07–0:10 — FULL FIT HERO MOMENT
Hard cut.
Full-body or three-quarter mirror view.
Hold this shot long enough for the viewer to inspect the jacket.

She turns gently to show:
front fit
side profile
shoulder volume
jacket length

No fast camera movement.

0:10–0:12 — DETAIL PROOF
Closer shot.
She adjusts the collar and lightly pulls the hem to show its actual structure.

She says:
“Yeah… this is pretty much exactly what I wanted.”

0:12–0:13 — END
Natural relaxed mirror glance.
No call-to-action.

VISUAL STYLE
Casual home review.
Smartphone camera.
Available daylight.
Slight handheld motion.
Natural autofocus.
No luxury fashion-commercial aesthetic.

AUDIO
Real clothing sounds.
Quiet room ambience.
Natural spoken dialogue.

IMPORTANT REALISM
Keep the jacket identical between every cut.
Correct hand-to-fabric contact.
Realistic textile compression and folds.
Correct mirror geometry.
No clothing-body intersections.
No unexplained garment state changes.

NO
generated captions
price overlays
rating graphics
cinematic zoom
dramatic reveal transition
fabric morph
product color drift
extra design details
forced influencer gestures
```

## Alternative concept 1 — Material + try-on proof

```text
Create a realistic 12-second vertical 9:16 smartphone UGC product-review video using the exact navy quilted puffer jacket from the product reference.

PRODUCT CONSISTENCY
Keep the jacket identical to the reference in every shot:
- exact navy color
- exact quilting pattern and stitch layout
- exact collar, zipper, cuffs, pockets, hem, and proportions
- same material finish and puffiness
- no added logos, labels, pockets, zippers, buttons, or decorative details
- do not change the jacket length or silhouette

CREATOR
A casually dressed female creator in a normal bright bedroom or dressing area.
Natural appearance, relaxed body language, no commercial-model posing.
Keep face, hair, body proportions, and outfit underneath the jacket consistent throughout the video.

CAMERA
Vertical smartphone footage.
Natural window light.
Mostly handheld or lightly static.
Small autofocus and exposure corrections are acceptable.
No cinematic orbit, dolly movement, studio lighting, slow motion, or polished commercial camera work.

0:00–0:02 — MATERIAL HOOK
Start close on the jacket already in the creator’s hands.
She lightly compresses one quilted section between her fingers and lets it recover naturally.
Keep the fabric texture and quilting clearly visible.

She says:
“Okay, this feels way nicer than I expected.”

0:02–0:05 — DETAIL CHECK
Hard cut.
Medium close-up of the creator inspecting the zipper, collar, sleeve, and stitching.
She runs one hand naturally over the fabric.
The jacket bends and folds realistically with gravity.

No dialogue.

0:05–0:08 — TRY-ON
Hard cut.
The creator puts on the exact same jacket.
Show a simple natural dressing motion rather than a stylized transition.
Sleeves, shoulders, and hem should move naturally as her arms enter the jacket.

0:08–0:11 — FIT PROOF
Hard cut to a mirror or front-facing smartphone shot.
Show the full upper-body fit clearly.
The creator turns slightly left and right so the viewer can judge the silhouette, puffiness, shoulder fit, and length.

She says:
“I actually really like the shape.”

0:11–0:12 — NATURAL VERDICT
She briefly looks at herself in the mirror, adjusts the hem once, and gives a restrained satisfied expression.

AUDIO
Natural room ambience.
Realistic clothing rustle and zipper sounds.
No loud music.
No voice-over narration.

REALISM CONSTRAINTS
Hands must remain anatomically correct.
The jacket must not morph while being worn.
Maintain realistic fabric weight, compression, drape, folds, and sleeve movement.
Do not make the fabric unnaturally rigid, glossy, inflatable, or weightless.
Mirror reflection must match the creator and garment correctly.

NEGATIVE CONSTRAINTS
No product redesign.
No instant outfit transformation.
No floating fabric.
No extra fingers.
No duplicated limbs.
No exaggerated smiling.
No runway walk.
No fashion-commercial posing.
No generated text or captions.
No logo card.
```

## Alternative concept 2 — Skeptical → impressed

```text
Create a realistic 12-second vertical 9:16 UGC review video of the exact navy quilted puffer jacket shown in the product reference.

The video should feel like a real social-media creator casually testing a jacket she was unsure about, not a fashion advertisement.

Lock all visible product details to the reference:
exact navy tone, quilting geometry, puffiness, zipper position, collar shape, pockets, cuffs, hem, material, and proportions.

0:00–0:02 — SKEPTICAL HOOK
The creator holds the folded jacket in front of herself and looks at it with mild uncertainty.

She says:
“I thought this was gonna look really bulky.”

Camera: handheld chest-height smartphone shot.

0:02–0:05 — QUICK INSPECTION
Hard cut.
She unfolds the jacket and checks the material and one sleeve.
The fabric falls naturally under gravity.

No dialogue.

0:05–0:08 — TRY-ON
Hard cut.
She puts the jacket on naturally.
Do not use a jump-cut transformation.
Show enough real dressing movement for the action to feel physically continuous.

0:08–0:11 — RESULT
Hard cut to a mirror view.
The jacket is fully worn.
She looks at the silhouette, turns slightly sideways, then faces forward again.

Her expression changes from doubtful to quietly impressed.

She says:
“Wait… this is actually really flattering.”

0:11–0:12
She lightly touches the collar and gives a small approving nod.

CAMERA AND STYLE
Ordinary bedroom or entryway.
Natural daylight.
Small handheld imperfections.
No cinematic lighting.
No camera orbit.
No beauty-commercial skin treatment.
No exaggerated reaction.

PHYSICS
The jacket must maintain realistic volume and weight.
Quilted panels should compress where touched and recover naturally.
Sleeves should bend correctly with elbow movement.
The hem should react naturally when the creator turns.
No cloth clipping into the body.

AUDIO
Room tone, clothing rustle, subtle zipper/fabric sounds.
Dialogue should sound casual and spontaneous.

AVOID
garment morphing
changing quilt patterns
wrong zipper
extra pockets
different collar
extreme oversized fit
instant wardrobe transformation
mirror mismatch
hand deformation
commercial posing
on-screen text
```

## Alternative concept 3 — Everyday routine / lifestyle

```text
Create a realistic 12-second vertical 9:16 smartphone UGC lifestyle-review video featuring the exact navy quilted puffer jacket from the product reference.

The video should feel like the creator is casually getting ready to leave home and realizing she likes the jacket.

Maintain exact jacket geometry, navy color, quilting, collar, zipper, pockets, cuffs, material, proportions, and fit across all shots.

0:00–0:02 — FIRST-FRAME HOOK
Creator is already wearing the jacket in front of a hallway mirror.
She quickly looks at the fit and says:

“Okay… this outfit is actually working.”

0:02–0:05 — NATURAL ADJUSTMENT
Close handheld shot.
She straightens the collar, lightly pulls one sleeve into place, and zips the jacket partway.

Show realistic fingers, zipper interaction, fabric resistance, and folds.

0:05–0:08 — FIT CHECK
Mirror shot.
She steps back once and turns slightly sideways.
Allow the viewer to clearly see the jacket silhouette and length.

No dialogue.

0:08–0:10 — REAL-LIFE MOVEMENT
Hard cut.
She picks up a small everyday bag or keys and takes two steps toward the door.
The jacket moves naturally with her shoulders and arms.

0:10–0:12 — CASUAL VERDICT
She glances once at the camera and says:

“Yeah, I’m keeping this one.”

Small natural smile, then exit frame.

CAMERA
Phone-camera realism.
Normal apartment or home hallway.
Natural daylight or ordinary room lighting.
Static mirror phone plus one handheld close-up.
No tracking rig or cinematic camera motion.

AUDIO
Soft room ambience.
Fabric rustle.
Zipper sound.
Footsteps.
No prominent soundtrack required.

REALISM
Natural jacket weight.
Realistic puffiness.
Correct sleeve bending.
Correct contact between hands and fabric.
No artificial wind.
No garment morphing between shots.
No exaggerated model posing.

AVOID
studio fashion shoot
beauty-commercial lighting
dramatic walking sequence
perfectly choreographed gestures
generated text
logos not in reference
extra garment features
unnatural cloth simulation
```

## What this case is intended to test

- whether a fashion prompt protects garment geometry through handling and try-on;
- whether the hero moment gives enough time to evaluate real-world fit;
- whether mirror shots preserve creator and garment continuity;
- whether textile weight, compression, drape, and sleeve movement remain plausible;
- whether multiple concepts genuinely change the narrative angle instead of only changing dialogue.

## Next step

Generate the recommended concept first. After a real output exists, add the video/contact sheet, score it with the QA dimensions, classify any failure tags, and create only the smallest repair needed for V02.
