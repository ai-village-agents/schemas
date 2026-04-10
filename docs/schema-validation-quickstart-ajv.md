# Schema validation quickstart with `ajv`

This short guide shows one concrete way to validate JSON documents
against the schemas in this repository using the [`ajv`](https://ajv.js.org/)
validator for Node.js. It is intentionally minimal and does not assume
any particular project structure.

## 1. Install dependencies

From your project directory (not necessarily this repo), install `ajv`
and a JSON loader such as `node-fetch` or the built-in `fs` module:

```bash
npm install ajv
```

If you prefer ESM with `fetch`, you can rely on the built-in `fetch`
available in recent Node.js versions.

## 2. Load a schema from this repository

You can either copy a schema file into your project (for a fixed
version) or load it directly from GitHub using the raw URL. For
example, to validate against `ai-village-agent-session-v1.2.json` from
this repository:

```js
import Ajv from "ajv";

const ajv = new Ajv({ allErrors: true, strict: false });

const schemaUrl = "https://raw.githubusercontent.com/ai-village-agents/schemas/main/ai-village-agent-session-v1.2.json";
const schema = await (await fetch(schemaUrl)).json();

const validate = ajv.compile(schema);
```

For long-lived systems you will usually want to pin to a specific
commit hash instead of `main` by replacing `main` in the URL with a
commit SHA.

## 3. Validate a document

Once you have a compiled validator, you can validate any JSON object:

```js
const data = JSON.parse(await fs.promises.readFile("session.json", "utf8"));

if (validate(data)) {
  console.log("session.json is valid!");
} else {
  console.error("session.json is invalid:", validate.errors);
}
```

This pattern works for all of the schemas in this repository. Pair it
with the versioning notes in the README: use `*-v1` schemas when you
want stability, and treat `v0.x` schemas as experimental by pinning to
exact versions.
