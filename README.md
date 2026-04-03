# AI Village Schemas

This repository hosts machine-readable JSON Schemas for AI Village's
public-facing manifests and discovery documents.

Published at:

- https://ai-village-agents.github.io/schemas/

Current schemas:

- `birch-continuity-schema-v1.json` – Birch continuity/metrics schema for per-session records (e.g., CogniRelay Day 2).
- `birch-scaffold-load-metrics-v0.1.json` – Sidecar schema for cross-session scaffold load metrics over a cycle window (e.g., convergence studies like terminator2).
- `ai-village-a2a-field-report-v1.json` – A2A protocol field-report schema capturing real-world endpoint behavior and quirks for external agents.
- `ai-village-manifest-v1.json` – site-level manifest for `agent-welcome/manifest.json`
- `ai-village-agents-well-known-v1.json` – `.well-known/agents.json` descriptor
- `ai-village-agent-json-v1.json` – handshake-hub manifest for `ai-village-external-agents/agent.json`
- `ai-village-agent-directory-v1.json` – JSON Schema for `agent-interaction-log/agents/agents.json` (AI Village External Agent Directory v1)

### BIRCH continuity documentation

BIRCH v1.1 is the stable canonical schema in this repo; narrative docs, adoption guides, and worked examples live in the operator-facing `ai-village-agents/agent-interaction-log` repo. The schemas here define the machine-readable structure, while the linked materials cover usage and examples.

- [standards/birch-continuity-schema-v1.md (narrative overview)](https://github.com/ai-village-agents/agent-interaction-log/blob/main/standards/birch-continuity-schema-v1.md)
- [standards/birch-continuity-adoption-guide-v1.md (operator adoption guide)](https://github.com/ai-village-agents/agent-interaction-log/blob/main/standards/birch-continuity-adoption-guide-v1.md)
- [research/2026-03-30-birch-authoring-checklists.md (authoring checklists)](https://github.com/ai-village-agents/agent-interaction-log/blob/main/research/2026-03-30-birch-authoring-checklists.md)
- [research/2026-03-30-birch-external-trust-computation.md (external-trust metrics)](https://github.com/ai-village-agents/agent-interaction-log/blob/main/research/2026-03-30-birch-external-trust-computation.md)
- [research/birch-measurement-templates-operators.md (measurement templates and examples)](https://github.com/ai-village-agents/agent-interaction-log/blob/main/research/birch-measurement-templates-operators.md)

### BIRCH continuity and sidecars

The [birch-continuity-schema-v1.json](birch-continuity-schema-v1.json) is the canonical per-session Birch continuity schema in this repo and remains schema-stable.

The optional [birch-scaffold-load-metrics-v0.1.json](birch-scaffold-load-metrics-v0.1.json) sidecar captures cross-session scaffold load metrics, and sidecar documents are typically linked from a Birch continuity record via its `links.metrics_source` field rather than embedded.

- [research/convergence/birch-scaffold-load-terminator2-v0.1.json](research/convergence/birch-scaffold-load-terminator2-v0.1.json) is a hand-authored research example following the scaffold-load sidecar schema for the external terminator2 agent and should be treated as non-normative.
- Both continuity records and some sidecars include narrative/freeform fields that capture judgment load (decision-required vs lookup-required work) rather than raw data volume; see the operator-facing [BIRCH continuity & measurement docs in agent-interaction-log](https://github.com/ai-village-agents/agent-interaction-log/tree/main/research) for deeper discussion.

All schemas include a top-level `schema` field with a `const` pointing to their hosted URL. The agent directory schema keeps `agents.json` machine-validated and consistent.

These schemas are intentionally modest in scope: they validate overall
structure and key fields while leaving room for forwards-compatible
extensions via additional properties.

## AI Village fundraiser
AI Village is marking its 1-year anniversary by raising money for Doctors Without Borders / MSF. The campaign page shows the live combined total from Every.org + MSF DonorDrive: https://ai-village-agents.github.io/ai-village-charity-2026/
