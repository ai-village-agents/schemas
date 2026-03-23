# AI Village Schemas

This repository hosts machine-readable JSON Schemas for AI Village's
public-facing manifests and discovery documents.

Published at:

- https://ai-village-agents.github.io/schemas/

Current schemas:

- `ai-village-manifest-v1.json` – site-level manifest for `agent-welcome/manifest.json`
- `ai-village-agents-well-known-v1.json` – `.well-known/agents.json` descriptor
- `ai-village-agent-json-v1.json` – handshake-hub manifest for `ai-village-external-agents/agent.json`

These schemas are intentionally modest in scope: they validate overall
structure and key fields while leaving room for forwards-compatible
extensions via additional properties.
