# FLOW-APPLIANCE-001 — evidence manifest

Status: **validated; V03 PASS**

## Reference

Product: countertop food processor / chopper.

The committed product reference remains the source of truth for appliance geometry, clear bowl, lid, right-side handle, central spindle, two front controls, scale, and visible branding.

## Artifact layout

```text
flow-appliance-001/
├── README.md
├── prompts/
│   └── v03-clip-2.md
├── qa/
│   ├── v02.md
│   └── v03.md
├── reference-product.jpg
├── v01-clip-1-preview.mp4
├── v01-clip-2-preview.mp4
├── v01-contact-sheet.jpg
├── v02-clip-1-preview.mp4
├── v02-clip-2-preview.mp4
├── v02-contact-sheet.jpg
├── v03-clip-2-preview.mp4
└── v03-contact-sheet.jpg
```

## Lifecycle

```text
V01
12-second story forced into 8-second generation behavior
→ temporal overload / weak hero isolation

V02
native split into two 8-second clips
→ clip 1 improved
→ clip 2 regressed to coarse ingredients before reveal

V03
targeted continuation-state repair
→ immutable finished opening state
→ PASS
```

## QA

- [V02 QA](qa/v02.md)
- [V03 QA](qa/v03.md)

## Prompts

- [V03 clip 2 repair prompt](prompts/v03-clip-2.md)

## Media

- [Product reference](reference-product.jpg)
- [V01 contact sheet](v01-contact-sheet.jpg)
- [V02 contact sheet](v02-contact-sheet.jpg)
- [V03 contact sheet](v03-contact-sheet.jpg)

## Canonical case

The narrative case file remains:

`examples/showcase/appliance-multistate-google-flow.md`

## Reusable lesson

For continuation clips, define an explicit continuity anchor, immutable opening state, forbidden regressions, and enough quiet hero time. V03 validated that this is more reliable than simply describing the clip as a continuation.
