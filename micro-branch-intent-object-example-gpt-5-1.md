# Micro-branch intent object v0.1 – tiny example (GPT-5.1, 2026-04-10)

This note shows a single concrete instance of `micro-branch-intent-object-v0.1.json`.
The intent object is meant to be small and branch-scoped: one snapshot of what a
branch is for, expressed using the From / To / Route pattern.

## Example instance

```json
{
  "schema_version": "0.1.0",
  "branchName": "gpt-5-1-micro-branch-intent-schema-v0.1",
  "from": "conceptual micro-branch postcards and intent-object reflections with no machine-checkable schema",
  "to": "an experimental JSON Schema that lets tools validate tiny intent records for individual branches",
  "route": "add micro-branch-intent-object-v0.1.json with required from/to/route fields and push it on a small feature branch",
  "tags": ["schemas", "micro-branch", "intent", "example"],
  "createdAt": "2026-04-10T00:00:00Z"
}
```

This instance is valid against `micro-branch-intent-object-v0.1.json` because it
provides all required fields (`schema_version`, `branchName`, `from`, `to`,
`route`) and only uses the optional properties allowed by the schema
(`tags`, `createdAt`). There are no extra keys.

To validate an object like this, load `micro-branch-intent-object-v0.1.json`
into your preferred JSON Schema validator (for example, Ajv in Node.js or
`jsonschema` in Python) and validate the instance above as usual.
