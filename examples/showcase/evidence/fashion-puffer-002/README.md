# FASHION-PUFFER-002 evidence

## Reference input

A navy quilted puffer jacket reference image was supplied for this case.

- Type: product/reference image
- Product: navy quilted puffer jacket
- Role: source of truth for garment color, quilting, geometry, material appearance, collar, zipper, sleeves, hem, and overall silhouette
- Repository media status: generated preview binaries are not currently committed in this evidence bundle

## Evidence index

- `v02-qa.md` — QA for V02 Clip 1: partial-state repair still skipped the physical try-on action via a temporal discontinuity.
- `v03-qa.md` — QA for V03 Clip 1: dedicated single-action repair still failed because the requested partial-worn opening state collapsed to a fully worn state.
- `v04-qa.md` — QA for V04 Clip 1: visual conditioning still failed to preserve the requested partial-worn opening state and the model reconstructed its own dressing sequence.
- Canonical case file: `examples/showcase/fashion-puffer-fit-proof.md`

## V01 generation status

Two native 8-second Google Flow / Veo preview clips were generated and reviewed.

### Clip 1

Status: **repair required — P1 Major**

Observed failure: the jacket-donning sequence breaks during the transition from holding the garment to wearing it. The garment appears to partially morph or snap onto the creator, with ambiguous arm-to-sleeve contact and weak cloth/body continuity.

Tags:

```text
HIGH_INTERACTION_RISK
FABRIC_PHYSICS
BODY_MECHANICS_ERROR
STATE_DISCONTINUITY
CONTACT_ERROR
PRODUCT_MORPH
```

Root cause: the shot requires the model to solve both arms, both sleeves, shoulder rotation, flexible quilted fabric, occlusion, and product geometry at the same time.

### Clip 2

Status: **preserve by default**

The already-worn fit sequence is substantially more stable than Clip 1 and should not be regenerated merely because the dressing interaction failed. Reuse it unless a separate QA issue is identified.

## V02 result

Status: **failed — P1 Major**

V02 reduced the full dressing action to a partial-state one-arm insertion. Product fidelity, creator continuity, hand quality, and material behavior improved, but the model still avoided the difficult interaction.

Observed state path:

```text
unworn / material inspection
→ cut
→ temporary empty-room / subject absence
→ cut
→ fully worn
```

The requested sleeve insertion was omitted.

Detailed QA: `v02-qa.md`

## V03 result

Status: **failed — P1 Major**

V03 dedicated the full 8-second clip to one left-arm sleeve insertion and removed material inspection, dialogue, zipper use, mirror reveal, and internal cuts.

The generated clip was visually cleaner, but the first frame already showed the jacket fully worn. The model substituted the requested try-on action with an already-worn sleeve/front-panel adjustment.

This indicates that the partial-worn state itself is unstable under text-only prompting in the tested workflow.

Detailed QA: `v03-qa.md`

## V04 result

Status: **failed — P1 Major**

V04 changed the experiment from text-only prompting to visual conditioning. The intended opening state was one arm already inserted, the opposite sleeve clearly empty, and the opposite arm fully outside the jacket.

The generated output still did not preserve that state. Instead, the model began from an earlier unworn / loosely draped state, reconstructed part of the dressing sequence, substituted sleeve/front-panel adjustment for the exact requested insertion, and only later reached a fully worn state.

The important finding is that **reference-image conditioning is not equivalent to literal first-frame conditioning** in the tested workflow.

Detailed QA: `v04-qa.md`

## Current failure progression

```text
V01
full dressing interaction
→ physical / morph failure

V02
reduced partial try-on after a cut
→ temporal skip / omitted action

V03
single action from text-defined partial state
→ opening-state collapse to fully worn

V04
visual/reference-conditioned partial state
→ reference state not preserved; model reconstructs earlier dressing sequence
```

The case has progressed from a general interaction-complexity problem to a more specific **state-representation and conditioning-mode problem**.

## V05 test direction

V05 should test **literal first-frame image-to-video conditioning**, not general reference-image conditioning.

The supplied still must be the actual first frame of the generated video and already show:

```text
right arm fully inserted
right hand outside cuff
right shoulder seated correctly
left sleeve visibly empty
left arm clearly outside jacket
jacket open
product geometry matching reference
```

Then the generation prompt should describe only the forward motion:

```text
preserve frame 1 exactly
→ left hand enters visible empty sleeve
→ forearm travels through sleeve
→ hand emerges from cuff
→ jacket settles
→ hold final state
```

Do not describe how the creator reached the partial state. The generation model should animate from it, not recreate it.

If the workflow cannot guarantee the supplied image is literal frame 1, classify the sleeve-insertion interaction as **unreliable for production** in that workflow.

## Evidence status

The case remains **in repair testing** and is not yet validated.

The canonical case narrative and V05 proposal live in:

`examples/showcase/fashion-puffer-fit-proof.md`

Detailed generation QA is intentionally kept in this evidence directory, matching the organization used by Showcase #1.
