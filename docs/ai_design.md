# AI Design

This document defines the AI layer for the first version of the project. It focuses on how the model should be used, what structured input it should receive, and what structured output it must return.

## AI Output Shape

The AI layer should return structured analysis rather than free-form prose.

The first version should produce a JSON-like structure with these top-level sections:

- `seo_structure`
- `messaging_clarity`
- `cta_usage`
- `content_depth`
- `ux_structural_concerns`
- `recommendations`

Each insight section should contain:

- `score`
- `insight`
- `metric_ref`

The `recommendations` section should contain 3 to 5 items. Each recommendation should include:

- `priority`
- `title`
- `reasoning`
- `action`
- `metric_ref`
- `expected_outcome`

This structure is intentionally explicit so the AI output can be validated, logged, and rendered cleanly in the CLI later.
