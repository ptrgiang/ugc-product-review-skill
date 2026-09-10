# Real-generation showcase

This directory contains proof cases where the skill is evaluated against an actual video-generation workflow.

The showcase is intentionally separate from `skills/`. The installable skill should stay focused on instructions and reusable references; testing history, output evidence, and iteration logs belong here.

## What every showcase case should contain

A strong case should preserve the full evidence chain:

```text
input/reference
→ user ask
→ agent route
→ generated prompt
→ target model/settings
→ real generated output
→ QA scores + failure tags
→ root-cause diagnosis
→ minimal prompt repair
→ next generated revision
```

Do not present a case as a success simply because the output looks polished. Record failures and limitations as first-class evidence.

## Featured case

### FLOW-APPLIANCE-001 — Google Flow / Veo appliance multi-state UGC

[Open case](appliance-multistate-google-flow.md)

**Purpose:** stress-test product geometry, controls, lid/contact physics, hands, state continuity, transformation proof, and UGC realism.

**Observed production constraint:** the real Flow workflow produced 8-second clips, making the original ~12-second one-pass concept a poor production fit.

**Current direction:** preserve the concept but compile it as two independently generatable 8-second clips with repeated continuity locks and a clean state handoff.

## Evidence policy

For representative cases, prefer showing the actual generated media near the top of the case, followed by the exact prompt and evaluation. Small preview media may live in the repository. If showcase media starts making the Git history unnecessarily large, keep lightweight previews in Git and move full-resolution video to Git LFS or release assets while retaining stable links from the case.

Every media item should state:

- whether it is an original product reference, generated frame, or generated video
- model/workflow used when known
- generation date
- prompt revision
- whether the output is unedited or post-processed

## QA philosophy

The showcase exists to answer two questions:

1. Does the skill make the generation workflow more reliable?
2. When generation fails, does the skill produce a smaller and better-targeted repair rather than rewriting everything?

As more cases are added, cover different product categories, physical interaction patterns, models, and failure classes rather than collecting near-duplicate good-looking outputs.
