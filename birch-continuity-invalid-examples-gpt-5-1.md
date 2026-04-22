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

---

The file:

- `example-birch-external-trust-and-trail-invalid-metric-epd-string.json`

starts from the valid example and changes a **single nested metric field**:
`metrics.denominator_metrics[0].epd` is set to the string `"14.0"` instead of
a JSON number. Under `birch-continuity-schema-v1.json`, this produces one
validation error at the path:

- `['metrics', 'denominator_metrics', 0, 'epd']` with a message like `"'14.0' is not of type 'number'".

This variant is useful for practicing how validators report **nested type
errors inside arrays of objects**, complementing the missing-`metrics` root
example above.

