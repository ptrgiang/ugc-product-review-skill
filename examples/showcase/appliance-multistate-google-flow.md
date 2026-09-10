# Showcase candidate: Appliance multi-state — Google Flow

Status: **awaiting real generation evidence**

This case is intentionally designed to stress the failure modes most relevant to appliance UGC: product geometry drift, control-panel drift, lid/contact physics, hand quality, state continuity, and hero-moment timing.

## Case ID

`FLOW-APPLIANCE-001`

## Product abstraction

Use a countertop kitchen appliance with:

- one removable container
- one locking lid
- one clearly visible control panel
- a visible before/after food or liquid transformation

If a real product/reference image is available, use it instead of inventing product geometry. Do not invent button labels, proprietary mechanisms, capacities, wattage, cycle names, or performance claims.

## Creative angle

**Skeptical → impressed fast demo**

Buyer doubt: does the appliance produce a visibly useful result without making the workflow feel complicated?

Primary visual proof: the same container is opened after processing and shows a clearly transformed result.

## Target structure

Vertical 9:16 creator-style video, approximately 12 seconds.

- **0:00–0:02 — result-first hook**: creator holds or reveals the finished removable container beside the appliance
- **0:02–0:05 — setup**: load/seat container and lock lid
- **0:05–0:07 — start**: one simple control interaction, appliance begins believable operation
- **0:07–0:10 — hero reveal**: processing is complete; creator unlocks/opens and shows transformed contents
- **0:10–0:12 — restrained verdict**: short natural reaction with the result still readable

## Google Flow / Veo-style production prompt — V01

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

## What V01 intentionally tests

V01 should reveal whether the model can handle:

- the same product across `finished → before processing → running → finished/opened`
- one lid interaction
- one control interaction
- one creator/product handoff
- a dedicated 1.5–2 second hero moment
- realistic UGC camera language without commercial over-polish

## Pass criteria

A showcase-quality result should satisfy all of the following:

- appliance silhouette and scale do not change
- container remains the same object
- lid geometry and attachment do not morph
- control count/layout do not change
- no invented control label is introduced
- hand contact is plausible during lid operation
- appliance stays physically supported while running
- transformed contents are visibly different from the input state
- hero result is readable for roughly 1.5 seconds or more
- final video still feels like creator-shot UGC

## Failure tags to watch

Use the QA taxonomy where applicable. Likely failures include:

- `PRODUCT_MORPH`
- `CONTROL_LAYOUT_ERROR`
- `HAND_DEFORMATION`
- `GRIP_ERROR`
- `HINGE_OR_LATCH_ERROR`
- `STATE_CONTINUITY_ERROR`
- `HERO_MOMENT_TOO_FAST`
- `PACING_ERROR`

## Result log

Fill this only after a real Flow generation.

```text
Date:
Flow model/version shown:
Settings/mode:
Reference assets:
Prompt revision: V01

Product fidelity: __ / 2
Creator continuity: __ / 2
Physical plausibility: __ / 2
Hand quality: __ / 2
State continuity: __ / 2
Hero clarity: __ / 2
UGC realism: __ / 2
Prompt adherence: __ / 2
TOTAL: __ / 16

Observed failure tags:
What worked:
What failed:
Highest-priority repair:
```

## Next revision

Do not write V02 in advance. Generate V01 first, inspect the actual failure, then change only the smallest prompt section responsible for that failure.
