import contextlib
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts.verify_artifact_manifest import main, verify_manifest


class ArtifactManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()
        (self.root / "docs" / "artifact.txt").write_bytes(b"review packet\n")
        self.manifest = self.root / "docs" / "manifest.json"

    def tearDown(self):
        self.temp.cleanup()

    def write_manifest(self, artifacts):
        self.manifest.write_text(
            json.dumps({"hashed_artifacts": artifacts}), encoding="utf-8"
        )

    def artifact(self, path="docs/artifact.txt"):
        digest = hashlib.sha256((self.root / path).read_bytes()).hexdigest()
        return {"path": path, "sha256": digest}

    def test_accepts_matching_artifact_hash(self):
        self.write_manifest([self.artifact()])
        self.assertEqual([], verify_manifest(self.manifest))

    def test_reports_missing_artifact(self):
        self.write_manifest([{"path": "docs/missing.txt", "sha256": "0" * 64}])
        self.assertIn("file is missing", verify_manifest(self.manifest)[0])

    def test_reports_modified_artifact(self):
        record = self.artifact()
        (self.root / "docs" / "artifact.txt").write_bytes(b"changed\n")
        self.write_manifest([record])
        self.assertIn("SHA-256 mismatch", verify_manifest(self.manifest)[0])

    def test_rejects_path_traversal_and_duplicate_paths(self):
        record = self.artifact()
        self.write_manifest([{"path": "../outside.txt", "sha256": "0" * 64}, record, record])
        errors = verify_manifest(self.manifest)
        self.assertTrue(any("stay inside repository" in error for error in errors))
        self.assertTrue(any("duplicate artifact path" in error for error in errors))

    def test_rejects_malformed_manifest(self):
        self.manifest.write_text("[]", encoding="utf-8")
        self.assertIn("hashed_artifacts array", verify_manifest(self.manifest)[0])

    def test_rejects_empty_artifact_list(self):
        self.write_manifest([])
        self.assertIn("must not be empty", verify_manifest(self.manifest)[0])

    def test_rejects_equivalent_path_spellings(self):
        record = self.artifact()
        alias = dict(record, path="docs/./artifact.txt")
        self.write_manifest([record, alias])
        self.assertIn("duplicate artifact path", verify_manifest(self.manifest)[0])

    def test_reports_invalid_path_without_raising(self):
        self.write_manifest([{"path": "docs/artifact.txt\0", "sha256": "0" * 64}])
        self.assertIn("invalid path", verify_manifest(self.manifest)[0])

    def test_cli_returns_failure_for_invalid_manifest(self):
        self.write_manifest([])
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            result = main([str(self.manifest)])
        self.assertEqual(1, result)
        self.assertIn("must not be empty", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
