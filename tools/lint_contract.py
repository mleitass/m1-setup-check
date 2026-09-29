#!/usr/bin/env python3
"""Validate an OpenAPI document and the FITA course contract rules."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from openapi_spec_validator import validate


HTTP_METHODS = {
    "get",
    "put",
    "post",
    "delete",
    "options",
    "head",
    "patch",
    "trace",
}
ERROR_SCHEMA_REF = "#/components/schemas/Error"
STATUS_CODE = re.compile(r"^[1-5][0-9X]{2}$", re.IGNORECASE)


def resolve_local_ref(document: dict[str, Any], ref: str) -> Any:
    """Resolve a JSON Pointer that points into the current document."""
    if not ref.startswith("#/"):
        return None

    value: Any = document
    for raw_part in ref[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def response_uses_error_schema(
    document: dict[str, Any], response: Any, seen_refs: set[str] | None = None
) -> bool:
    """Return whether a response ultimately references the shared Error schema."""
    if not isinstance(response, dict):
        return False

    ref = response.get("$ref")
    if isinstance(ref, str):
        if ref == ERROR_SCHEMA_REF:
            return True
        seen_refs = set() if seen_refs is None else seen_refs
        if ref in seen_refs:
            return False
        target = resolve_local_ref(document, ref)
        return response_uses_error_schema(document, target, seen_refs | {ref})

    content = response.get("content")
    if not isinstance(content, dict):
        return False

    for media_type in content.values():
        if not isinstance(media_type, dict):
            continue
        schema = media_type.get("schema")
        if isinstance(schema, dict) and schema.get("$ref") == ERROR_SCHEMA_REF:
            return True
    return False


def iter_operations(document: dict[str, Any]):
    paths = document.get("paths", {})
    if not isinstance(paths, dict):
        return
    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method.lower() in HTTP_METHODS and isinstance(operation, dict):
                yield str(path), method.upper(), operation


def course_rule_errors(document: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for path, method, operation in iter_operations(document):
        label = f"{method} {path}"
        raw_responses = operation.get("responses")
        if not isinstance(raw_responses, dict):
            errors.append(f"{label}: nav deklarēts responses objekts")
            continue

        responses = {str(code).upper(): response for code, response in raw_responses.items()}
        for required in ("400", "404"):
            if required not in responses:
                errors.append(f"{label}: nav deklarēta {required} atbilde")

        if not any(code == "5XX" or re.fullmatch(r"5\d\d", code) for code in responses):
            errors.append(f"{label}: nav deklarēta 5xx atbilde")

        for code, response in responses.items():
            if STATUS_CODE.fullmatch(code) and code[0] in {"4", "5"}:
                if not response_uses_error_schema(document, response):
                    errors.append(
                        f"{label}: {code} atbilde neizmanto kopīgo "
                        f"{ERROR_SCHEMA_REF} shēmu ar $ref"
                    )

    return errors


def load_document(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        document = yaml.safe_load(stream)
    if not isinstance(document, dict):
        raise ValueError("OpenAPI dokumenta saknei jābūt objektam")
    return document


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validē OpenAPI dokumentu un FITA kursa līguma noteikumus."
    )
    parser.add_argument("contract", type=Path, help="Ceļš uz OpenAPI YAML vai JSON failu")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        document = load_document(args.contract)
        validate(document)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"OpenAPI validācijas kļūda: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # validator exception types differ between releases
        print(f"OpenAPI validācijas kļūda: {exc}", file=sys.stderr)
        return 1

    errors = course_rule_errors(document)
    if errors:
        print("Kursa līguma noteikumi nav izpildīti:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.contract} ir derīgs un atbilst kursa noteikumiem")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
