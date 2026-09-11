# Showcase #1: Appliance multi-state — Google Flow

Status: **completed repair lifecycle; V03 PASS**

This case stress-tests the failure modes most relevant to appliance UGC: product geometry drift, control-panel drift, lid/contact physics, hand quality, state continuity, hero-moment timing, and the practical effect of model clip-duration constraints.

## At a glance

**Case ID:** `FLOW-APPLIANCE-001`

**Product/category:** Countertop food processor / appliance

**Workflow/model:** Google Flow / Veo

**Creative angle:** Skeptical → impressed fast demo

**Primary visual proof:** The same clear bowl moves from coarse salsa ingredients to a visibly processed chunky salsa result.

**Lifecycle:** `V01 → V02 → V03 → PASS`

**V01 QA:** `13 / 16`

**V03 QA:** `15 / 16`

**Current result:** V03 fixes the continuation-state regression observed in V02 by enforcing an immutable post-processing opening state. No V04 is required for this root cause.

## Product reference

The real test used a white countertop food processor/chopper with:

- one clear removable processing bowl
- one clear locking lid
- a right-side clear handle
- a central white spindle
- two circular controls on the lower front body
- a visible chopped-food transformation

The original reference image remains the authority for geometry, proportions, color, materials, control placement, handle placement, lid design, bowl scale, and visible branding. No prompt revision may invent extra controls, labels, modes, capacities, wattage, or proprietary features.

[View the product reference →](evidence/flow-appliance-001/reference-product.jpg)

## Creative objective

The test asks a simple buyer question: can the appliance produce a visibly useful result without making the workflow feel complicated?

The intended story is:

```text
coarse ingredients
→ close / lock
→ press control / process
→ processing finishes
→ open lid
→ reveal finished salsa
→ restrained verdict
```

The difficult part is not just generating attractive shots. The same appliance, bowl, controls, creator session, and food state must remain causally coherent across multiple generated clips.

---

# V01 — Original 12-second design

## Original target structure

```text
0:00–0:02 — result-first hook
0:02–0:05 — setup
0:05–0:07 — start
0:07–0:10 — hero reveal
0:10–0:12 — restrained verdict
```

## V01 prompt

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

## V01 real-generation result

**Generation date:** 2026-09-10

**Observed practical workflow constraint:** the tested Flow workflow generated 8-second clips, so the 12-second design did not fit cleanly as one native generation.

The attempt therefore produced two 8-second outputs:

- `v01-clip-1` — setup / product interaction / processing-oriented footage
- `v01-clip-2` — processed salsa / reveal / verdict-oriented footage

### V01 evidence

**Clip 1 — setup / processing**

https://github.com/user-attachments/assets/71937adb-04bc-4c5a-8eb2-d10db02e70ea

**Clip 2 — reveal / verdict**

https://github.com/user-attachments/assets/90213915-376f-4d0a-9afb-f6f9f1cb88e8

![V01 contact sheet](evidence/flow-appliance-001/v01-contact-sheet.jpg)

## V01 QA

| Dimension | Score | Observation |
| --- | ---: | --- |
| Product fidelity | 2 / 2 | White body, clear bowl, right-side handle, central spindle, and two-control layout remain recognizably stable. |
| Creator continuity | 2 / 2 | No major creator discontinuity in the useful footage. |
| Physical plausibility | 2 / 2 | Core lid/bowl/product interactions are generally believable. |
| Hand quality | 2 / 2 | Hands are usable and do not dominate the failure profile. |
| State continuity | 1 / 2 | Cross-clip state handoff needs stronger explicit control. |
| Hero clarity | 1 / 2 | Salsa result exists, but the payoff is not isolated strongly enough. |
| UGC realism | 1 / 2 | Creator-style framing works, but the final thumbs-up feels generic and ad-like. |
| Prompt adherence | 2 / 2 | Core appliance demo and result sequence were substantially followed. |
| **Total** | **13 / 16** | Useful result, but not yet a finished showcase-quality creative. |

### V01 diagnosis

The main root cause was temporal overload. Five narrative states were designed for approximately 12 seconds, while the tested workflow operated more reliably as shorter native clips.

This caused two downstream problems:

1. too much narrative responsibility per clip, leaving insufficient dedicated hero-proof time;
2. the ending collapsed into generic ad shorthand rather than a natural result-focused reaction.

### V01 failure tags

- `HERO_MOMENT_TOO_FAST`
- `TOO_COMMERCIAL`
- `PACING_ERROR`

---

# V02 — Native 2 × 8-second split

## Repair strategy

V02 made the smallest production-level changes necessary:

- compile the story natively as **2 × 8-second clips**;
- assign each clip one main physical objective;
- repeat critical product/reference locks in both clips;
- define a state handoff between clips;
- create a stronger coarse-ingredient versus processed-salsa contrast;
- reserve dedicated screen time for the hero result;
- replace the generic thumbs-up with a restrained result-focused reaction.

## Shared continuity lock

Use the supplied product reference as the visual authority in both clips. Preserve the same white appliance body, clear bowl, clear locking lid, right-side handle, central spindle, two circular front controls, logo placement if visible, countertop scale, creator, wardrobe, bright ordinary home kitchen, daylight direction, and smartphone UGC character.

## V02 clip 1 — Setup → Start

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

```text
same appliance
+ same bowl
+ same lid
+ same handle orientation
+ same creator session
+ processing underway
```

## V02 clip 2 — Intended Hero Result → Verdict

```text
Create an 8-second vertical 9:16 realistic smartphone UGC clip that continues the same food-processor review in the same kitchen.

Use the same supplied product reference as the exact authority. The white body, clear bowl, right-side handle, clear lid, central spindle, two circular front controls, logo placement, proportions, materials, scale, creator, wardrobe, counter position, and daylight must match the first clip. Do not add or redesign anything.

The food state is now clearly processed: instead of large separate tomato/onion/herb chunks, the bowl contains a visibly finer, evenly chopped fresh salsa mixture. Keep it believable for a food processor; do not turn it into an impossible smooth liquid or make the bowl refill itself.

0:00–0:03 — OPEN
The appliance is stopped and fully supported. One hand stabilizes the bowl/product while the other releases and opens the real lid in one simple motion. Preserve lid and handle geometry. Natural latch/contact sound is audible.

0:03–0:06 — HERO RESULT
Hold a stable medium-close view of the opened bowl for about 2 seconds with almost no camera movement. Make the finer salsa texture immediately readable. The product body and result remain visible together. No dialogue over the first part of the reveal.

0:06–0:08 — NATURAL VERDICT
Instead of a thumbs-up or presenter pose, the creator keeps attention on the food and says: “Okay, that came out way better than I expected.”

Keep the delivery observational, not salesy. No broad grin, no pointing at the product, no product beside the face, no commercial end pose.
```

## V02 real-generation result

V02 confirmed that splitting the story into two short outputs was the correct production strategy. Clip 1 became materially cleaner: the product remained readable, the coarse ingredient state was clear, the lid interaction was simpler, and the front controls stayed recognizable.

However, V02 exposed a new and more specific failure in clip 2.

### V02 evidence

**Clip 1 — ingredient proof / start**

https://github.com/user-attachments/assets/aa72da59-b23f-47be-956e-db1ed5cb4193

**Clip 2 — failed continuation reveal**

https://github.com/user-attachments/assets/1c47f50f-60c2-4bc7-acf0-50fa75b018b6

![V02 contact sheet](evidence/flow-appliance-001/v02-contact-sheet.jpg)

[Read the detailed V02 QA →](evidence/flow-appliance-001/v02-qa.md)

## V02 primary failure

Clip 2 did **not** begin in the required post-processing state.

The generated sequence effectively became:

```text
raw / coarse ingredients
→ lid opens
→ processed salsa appears
```

But the intended sequence was:

```text
processing already finished before clip starts
→ finished salsa already exists under the closed lid
→ lid opens
→ the same finished salsa is revealed
```

This is a first-frame continuation-state regression, not primarily a product-identity failure.

### V02 failure tags

- `STATE_DISCONTINUITY`
- `NO_CAUSAL_TRANSITION`
- `LID_GEOMETRY_DRIFT` — minor

## V02 root cause

A continuity description is not the same thing as an opening-state lock.

The V02 prompt described clip 2 as a continuation after processing, but it did not constrain the first frame strongly enough to stop the model from reconstructing the visually familiar coarse-ingredient setup before performing the reveal.

That observation led directly to V03.

---

# V03 — Targeted continuation-state repair

V03 keeps **V02 clip 1 unchanged** and regenerates **clip 2 only**.

The repair introduces one major concept: an explicit **immutable opening state** plus forbidden regressions.

## V03 targeted repair prompt

```text
TITLE
Food Processor Salsa Review — V03 Clip 2 — Finished-State Reveal Repair

OBJECTIVE
Create an 8-second vertical 9:16 realistic smartphone UGC continuation clip.
This clip begins after the processing shown in V02 clip 1 has fully finished.
The only goal is to reveal the already-finished salsa and give a restrained natural verdict.

REFERENCE PRIORITY
1. Use the original supplied product reference as the authority for appliance geometry, color, materials, bowl, lid, right-side handle, central spindle, controls, scale, and visible branding.
2. Use V02 clip 1 only as the continuity reference for creator, wardrobe, kitchen, daylight, counter position, framing character, and overall product placement.
If V02 clip 1 conflicts with the original product reference, preserve the original product reference.

CONTINUITY LOCK
Keep the exact same white appliance body, proportions, clear processing bowl, clear locking lid, right-side clear handle, central spindle, two circular front controls, creator, wardrobe, kitchen, countertop position, daylight direction, and casual smartphone UGC character.
Do not redesign, add, remove, move, or simplify any product part.

IMMUTABLE OPENING STATE — CRITICAL
The processing cycle has already fully finished before the first frame of this clip.
At frame 1:
- the same bowl is attached to the same appliance;
- the machine is stopped;
- the lid is fully closed and locked;
- the contents underneath the closed lid are already the final processed chunky salsa;
- no raw or coarse pre-processing ingredients exist anywhere in this clip.

This finished food state is immutable.
Opening the lid does not cause, trigger, or complete any transformation.
The salsa must already be processed before the lid starts moving.

FORBIDDEN REGRESSIONS
Never show the earlier coarse/raw ingredient state.
Never reset the bowl to the pre-processing state.
Never morph the contents during or after lid movement.
Never make finished salsa suddenly appear after the lid opens.
No second processing event occurs in this clip.

CAMERA / STYLE
Natural bright home-kitchen daylight. Vertical 9:16 casual smartphone UGC. Stable medium-close counter-height framing, slight human handheld imperfection only. Product and bowl readable. No cinematic orbit, no studio ad lighting, no generated captions, no logo card.

TIMELINE
0:00–0:02 — OPEN ALREADY-FINISHED BOWL
Start on the stopped appliance with the lid still closed.
One hand stabilizes the bowl/appliance. The other releases and lifts the existing lid in one simple physically plausible motion.
As the lid lifts, the same already-finished chunky salsa is continuously visible underneath. Its texture does not change.
Natural latch/contact sound. No dialogue.

0:02–0:05 — HERO PROOF
Hold a stable close-medium view of the open bowl and appliance for about 3 seconds.
Make the finished chunky salsa texture easy to read.
No dialogue during the clearest first 1.5–2 seconds of this hero hold.
No stirring, pouring, or other action that obscures the result.

0:05–0:08 — NATURAL VERDICT
Keep the result visible.
The creator briefly looks from the salsa to the phone with a small impressed reaction and says:
“Okay... that actually came out really good.”
No thumbs-up, pointing, broad grin, product beside face, or commercial presenter pose.
Finish as though the creator is about to keep using or tasting the result.

AUDIO
Natural kitchen room tone + lid/latch contact + natural voice.
No dramatic music.

PHYSICS / PRODUCT FIDELITY
Realistic hand grip and product weight. Stable bowl attachment. Correct lid geometry. Same handle direction. Same control layout. No floating parts, deformed hands, changing product scale, logo drift, control drift, lid morphing, or impossible food physics.

PASS CONDITION
V03 only passes if the very first visible food state is already processed salsa and that exact processed state remains unchanged through lid opening and hero reveal.
```

[Open the standalone V03 repair prompt →](evidence/flow-appliance-001/v03-clip-2-prompt.md)

## V03 real-generation result

V03 fixes the primary V02 failure.

At the opening of the regenerated clip, the contents are already in the processed salsa state before the lid is lifted. Lid opening now reveals the existing result instead of causing or coinciding with a hidden transformation.

The product stays recognizable, the finished result receives dedicated hero time, and the creator reaction remains restrained and review-like rather than collapsing into a generic presenter gesture.

### V03 evidence

**Clip 2 — targeted repair**

https://github.com/user-attachments/assets/b286e7c8-c2ea-4385-b421-6044d13a2cc9

![V03 contact sheet](evidence/flow-appliance-001/v03-contact-sheet.jpg)

[Read the detailed V03 QA →](evidence/flow-appliance-001/v03-qa.md)

## V03 QA

| Dimension | Score | Observation |
| --- | ---: | --- |
| Product fidelity | 2 / 2 | Appliance body, clear bowl, handle orientation, and control layout remain recognizable. |
| State continuity | 2 / 2 | Finished salsa exists before lid opening; no regression to the raw ingredient state. |
| Physical plausibility | 2 / 2 | The reveal is causally valid and the product stays supported. |
| Hand / lid interaction | 1.5 / 2 | Usable and plausible, though still slightly generated in smoothness. |
| Hero clarity | 2 / 2 | Processed result is readable and receives dedicated screen time. |
| UGC authenticity | 2 / 2 | Reaction is restrained and product-focused rather than overtly commercial. |
| Prompt adherence | 2 / 2 | The critical immutable opening-state instruction is followed. |
| Pacing | 1.5 / 2 | Strong overall; hero hold could be marginally more static. |
| **Total** | **15 / 16** | Targeted repair succeeds; no V04 required for this root cause. |

### Resolved errors

- `STATE_DISCONTINUITY`
- `NO_CAUSAL_TRANSITION`

### Remaining minor note

Slight lid/hand interaction smoothness remains, but it is below the threshold for another repair cycle.

---

# V01 → V02 → V03 comparison

| Dimension | V01 | V02 | V03 |
| --- | --- | --- | --- |
| Temporal design | 12-second story compressed into tested short-clip workflow | Native 2 × 8s split | Keeps split; repairs clip 2 only |
| Product fidelity | Good | Good | Good |
| State continuity | Fragile across clips | Fails at clip-2 opening state | Passes with immutable opening state |
| Hero clarity | Weak / compressed | Better structure, but causally invalid reveal | Clear, stable, causally valid reveal |
| UGC authenticity | Generic thumbs-up weakens ending | More restrained | Restrained and product-focused |
| Repair scope | — | Production architecture rewrite | Minimal targeted state repair |
| Final status | Needs repair | Needs targeted repair | **PASS** |

## Final lifecycle

```text
V01 — temporal overload / weak hero
↓
V02 — split-clip strategy improves execution but exposes state regression
↓
V03 — immutable opening-state repair resolves the regression
↓
PASS
```

## Production lesson

The strongest reusable lesson from this case is:

```text
continuity description ≠ opening-state lock
```

For fragile continuation clips, define all four explicitly:

1. **continuity anchor** — which prior output/reference must be matched;
2. **immutable opening state** — what is already true before frame 1;
3. **forbidden regressions** — which earlier states must never reappear;
4. **hero isolation** — enough quiet, stable screen time for the proof.

A prompt can describe continuity correctly and still allow a model to reconstruct an earlier state. When a transformation happened off-screen between clips, the first frame of the continuation needs its own explicit state contract.

## Decision

**PASS — Showcase #1 is complete.**

No V04 should be created unless a future regeneration exposes a different material failure.

## Evidence bundle

[Open the complete evidence bundle →](evidence/flow-appliance-001/README.md)
