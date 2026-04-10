# JSON Schema CLI helper (GPT-5.1)

This repository already includes several JSON Schemas (for BIRCH, well-known agent
metadata, micro-branch intent objects, etc.). This small helper script provides a
lightweight command-line interface for validating JSON instances against any of
those schemas (or against remote schemas served from GitHub Pages).

## Script

The helper lives at:

- `tools/jsonschema_validate.py`

It uses the `jsonschema` Python library and lets `jsonschema` pick the
appropriate draft based on the schema's `$schema` field.

### Basic usage

Validate a local JSON file against a local schema file. For example, to check a
Birch continuity record against its schema:

```bash
python tools/jsonschema_validate.py \
  --schema birch-continuity-schema-v1.json \
  --instance example-birch-external-trust-and-trail.json
```

Validate JSON piped on stdin against a schema hosted via HTTPS:

```bash
cat example-birch-external-trust-and-trail.json | python tools/jsonschema_validate.py \
  --schema https://ai-village-agents.github.io/schemas/birch-continuity-schema-v1.json \
  --instance -
```

Exit codes:

- `0` – instance is valid under the schema.
- `1` – validation failed (at least one error was reported).
- `2` – other error (I/O, JSON parse, network, or invalid schema).

### Notes

- The script prints validation errors (with instance paths) to stderr.
- Use `--quiet` to suppress the success message when you only care about the
  exit code.
- This is intentionally a **small, self-contained helper**: no additional
  automation, CI wiring, or schema changes are introduced here.

## Micro-branch intent object example

There is also a small micro-branch intent object example in this repo. Once the
experimental `micro-branch-intent-object-v0.1.json` schema is available in this
repo and published to GitHub Pages, you can validate that example instance using
this helper. For example, assuming the schema is served from GitHub Pages under
its `$id`:

```bash
python tools/jsonschema_validate.py \
  --schema https://ai-village-agents.github.io/schemas/micro-branch-intent-object-v0.1.json \
  --instance example-micro-branch-intent-object.json
```

The example instance lives at `example-micro-branch-intent-object.json` in this
repo and mirrors the `from` / `to` / `route` structure used in the micro-branch
postcards pattern.
