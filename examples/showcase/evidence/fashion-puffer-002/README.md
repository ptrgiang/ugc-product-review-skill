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

## Current hypothesis

The failure progression is now:

```text
V01
full dressing interaction
→ physical/morph failure

V02
reduced partial try-on after a cut
→ temporal skip / omitted action

V03
single action from text-defined partial state
→ opening-state collapse to fully worn
```

The case has therefore moved from a general interaction-complexity problem toward an **intermediate-state representation failure**.

## V04 test direction

V04 should test **visual start-frame conditioning** instead of another text-only repair.

Supply a reference/start frame that already shows the exact intended intermediate state:

```text
right arm fully inserted
right hand outside cuff
right shoulder loaded correctly
left sleeve visibly empty
left arm clearly outside jacket
jacket open
product geometry matching reference
```

Then ask the model to perform only one motion:

```text
preserve supplied start state
→ slowly insert left arm into visible left sleeve
→ left hand emerges from cuff
→ jacket settles
→ hold completed state
```

## Evidence status

The case remains **in repair testing** and is not yet validated.

The canonical case narrative and V04 proposal live in:

`examples/showcase/fashion-puffer-fit-proof.md`

Detailed generation QA is intentionally kept in this evidence directory, matching the organization used by Showcase #1.
