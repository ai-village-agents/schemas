#!/usr/bin/env python3
"""Simple JSON Schema CLI validator (GPT-5.1)

Usage examples:

  # Validate instance.json against local schema file
  python tools/jsonschema_validate.py --schema micro-branch-intent-object-v0.1.json --instance example.json

  # Validate JSON piped on stdin against a remote schema URL
  cat example.json | python tools/jsonschema_validate.py \
      --schema https://example.org/schemas/micro-branch-intent-object-v0.1.json \
      --instance -

The script exits with:
  0 on success (instance is valid),
  1 if validation fails,
  2 on other errors (I/O, JSON parse, network, etc.).
"""

import argparse
import json
import sys
import urllib.request
from typing import Any, Dict

import jsonschema
from jsonschema import validators


def load_json_from_path(path: str) -> Any:
    """Load JSON from a local file path.

    Raises OSError or json.JSONDecodeError on failure.
    """

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_json_from_url(url: str) -> Any:
    """Load JSON from a URL via HTTP(S).

    Raises URLError or json.JSONDecodeError on failure.
    """

    with urllib.request.urlopen(url) as resp:  # type: ignore[call-arg]
        charset = resp.headers.get_content_charset() or "utf-8"
        data = resp.read().decode(charset)
    return json.loads(data)


def load_schema(schema_ref: str) -> Dict[str, Any]:
    """Load a JSON Schema from a local path or URL."""

    if schema_ref.startswith("http://") or schema_ref.startswith("https://"):
        return load_json_from_url(schema_ref)
    return load_json_from_path(schema_ref)


def load_instance(instance_ref: str) -> Any:
    """Load a JSON instance from a path or stdin ('-')."""

    if instance_ref == "-":
        try:
            text = sys.stdin.read()
        except KeyboardInterrupt:
            raise
        if not text.strip():
            raise ValueError("No JSON data received on stdin")
        return json.loads(text)
    return load_json_from_path(instance_ref)


def build_validator(schema: Dict[str, Any]) -> jsonschema.protocols.Validator:
    """Construct an appropriate jsonschema validator for the given schema."""

    # Let jsonschema choose the most appropriate validator class based on $schema.
    ValidatorCls = validators.validator_for(schema)
    ValidatorCls.check_schema(schema)
    return ValidatorCls(schema)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a JSON instance against a JSON Schema.")
    parser.add_argument(
        "--schema",
        "-s",
        required=True,
        help="Path or URL of the JSON Schema to use.",
    )
    parser.add_argument(
        "--instance",
        "-i",
        default="-",
        help="Path to JSON instance to validate, or '-' to read from stdin (default).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress success output; still prints validation errors to stderr.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    try:
        schema = load_schema(args.schema)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to load schema from {args.schema!r}: {exc}", file=sys.stderr)
        return 2

    try:
        instance = load_instance(args.instance)
    except Exception as exc:  # noqa: BLE001
        target = "stdin" if args.instance == "-" else args.instance
        print(f"Failed to load JSON instance from {target!r}: {exc}", file=sys.stderr)
        return 2

    try:
        validator = build_validator(schema)
    except Exception as exc:  # noqa: BLE001
        print(f"Schema is not valid according to jsonschema: {exc}", file=sys.stderr)
        return 2

    errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
    if errors:
        for err in errors:
            location = "".join(f"[{repr(p)}]" for p in err.path)
            if location:
                prefix = f"instance{location}: "
            else:
                prefix = "instance: "
            print(prefix + err.message, file=sys.stderr)
        return 1

    if not args.quiet:
        print("OK: instance is valid under the provided schema.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv[1:]))
