# Benchmarks

The project does not currently claim model-quality benchmark scores.

This page defines the benchmark direction so future performance claims can be reproducible.

## Proposed evaluation dimensions

- product fidelity
- creator identity consistency
- hand accuracy
- physical plausibility
- hero-moment clarity
- UGC authenticity
- prompt compactness
- concept diversity across batches

## Evaluation fixture format

Each fixture should include:

- product category
- product/reference description
- user request
- expected module routing
- expected creative decision
- critical constraints
- expected failure conditions

Generated-video evaluation may additionally include human or model-assisted ratings, but the scoring method and model/version must be documented.

## Benchmark principles

- publish the inputs used
- distinguish structural tests from visual-quality tests
- do not compare video models without controlling prompt/model version
- report failures, not only successful generations
- keep subjective UGC-realism scoring separate from objective continuity failures

Until a reproducible benchmark exists, README claims should remain qualitative.
