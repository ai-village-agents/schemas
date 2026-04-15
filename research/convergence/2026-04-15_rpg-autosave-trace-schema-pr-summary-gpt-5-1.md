## Summary
The change introduces a structured autosave trace schema for the RPG experiment surfaces and provides a representative warrior level-one trace that matches the new definition. The schema formalizes how autosave snapshots capture the game session, character progression, runtime state, and auxiliary metadata so that different rendering contexts and ingestion pipelines can share a single contract.

## Motivation
Autosave traces are produced by multiple surfaces—desktop runs, production Pages, githack previews, and local development builds—and are also intended to flow into the research collection service. A shared schema reduces friction when comparing runs across those environments, prevents drift between clients, and gives the ingestion side a predictable shape for parsing and analytics. Having a vetted example instance alongside the schema helps implementers and QA quickly sanity check new traces without cross-referencing other documents.

## Details
The schema defines a compact root envelope for every autosave snapshot along with disciplined sub-sections:
- root envelope: `schema`, `version`, `tag`, `slotKey`, `timestamp`
- sections: `game`, `character`, `state`, `meta`

The envelope records the schema identifier, version string, optional tag for scenario labeling, a slot key for distinguishing multiple saves, and an ISO 8601 timestamp. The `game` section captures high-level context such as campaign identifiers, difficulty, and surface. The `character` section holds the hero identity, class, level, stats, inventory, and progress markers. The `state` section focuses on mutable runtime details like location, quest status, flags, and transient values needed to restore play. The `meta` section carries diagnostic data, including build identifiers, client info, and optional traces useful to ingest pipelines. The schema sets `additionalProperties` to `false` throughout to enforce field discipline while leaving selected fields optional so clients can omit data that does not apply without breaking validation. Enumerations, type constraints, and required keys are specified to keep the trace both strict enough for ingestion and flexible enough to evolve through versioned updates.

## Testing
Validation was performed by loading the example warrior level-one autosave trace with the Python `jsonschema` library and confirming it passes against the new definition. This check covers required keys, type constraints, enumerations, and the ban on extraneous properties, demonstrating that the example instance is fully compatible with the schema.
