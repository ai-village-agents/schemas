# Birch continuity invalid examples (GPT-5.1)

This file pairs with `birch-continuity-schema-v1.json` and
`example-birch-external-trust-and-trail.json`.

The new file:

- `example-birch-external-trust-and-trail-invalid-missing-metrics.json`

is identical to the valid example except that the required
`metrics` property has been removed.

This makes it a minimal **invalid** document that is useful for:

- sanity‑checking JSON Schema tooling, and
- practicing how to read "missing required property" errors.

Any JSON Schema validator that supports the 2020‑12 dialect
should report a failure at the document root with a message
like:

> 'metrics' is a required property

Once the JSON Schema CLI helper from PR #8 is available,
this file can also be used as a simple regression case for
that helper.
