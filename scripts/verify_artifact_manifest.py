#!/usr/bin/env python3
"""Verify SHA-256 entries in a draft artifact manifest.

Run from any directory with:
  python scripts/verify_artifact_manifest.py path/to/manifest.json

Manifest artifact paths are interpreted relative to the repository root (the
parent of the manifest's ``docs`` directory, or the manifest directory when
used with a standalone manifest). This checks byte integrity only; it does not
verify approval, authorship, or the truth of artifact contents.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def repository_root(manifest_path):
    manifest_path = manifest_path.resolve()
    if manifest_path.parent.name == "docs":
        return manifest_path.parent.parent
    return manifest_path.parent


def verify_manifest(manifest_path):
    """Return a list of verification errors; an empty list means valid."""
    manifest_path = Path(manifest_path)
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"cannot read manifest: {exc}"]

    artifacts = data.get("hashed_artifacts") if isinstance(data, dict) else None
    if not isinstance(artifacts, list):
        return ["manifest must contain a hashed_artifacts array"]

    root = repository_root(manifest_path)
    errors = []
    seen = set()
    for index, artifact in enumerate(artifacts):
        label = f"hashed_artifacts[{index}]"
        if not isinstance(artifact, dict):
            errors.append(f"{label}: expected an object")
            continue
        relative = artifact.get("path")
        expected = artifact.get("sha256")
        if not isinstance(relative, str) or not relative:
            errors.append(f"{label}: path must be a non-empty relative path")
            continue
        relative_path = Path(relative)
        if relative_path.is_absolute() or ".." in relative_path.parts:
            errors.append(f"{label} ({relative}): path must stay inside repository")
            continue
        normalized = relative_path.as_posix()
        if normalized in seen:
            errors.append(f"{label} ({relative}): duplicate artifact path")
            continue
        seen.add(normalized)
        if not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
            errors.append(f"{label} ({relative}): sha256 must be 64 hexadecimal characters")
            continue

        artifact_path = (root / relative_path).resolve()
        try:
            artifact_path.relative_to(root)
        except ValueError:
            errors.append(f"{label} ({relative}): resolved path escapes repository")
            continue
        try:
            actual = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
        except OSError:
            errors.append(f"{label} ({relative}): file is missing or unreadable")
            continue
        if actual.lower() != expected.lower():
            errors.append(f"{label} ({relative}): SHA-256 mismatch")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "manifest",
        help="manifest JSON path",
    )
    args = parser.parse_args(argv)
    errors = verify_manifest(args.manifest)
    if errors:
        print("Artifact manifest verification failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Artifact manifest verified: {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
