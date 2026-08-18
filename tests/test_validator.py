from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_prompts.py"
SPEC = importlib.util.spec_from_file_location("validate_prompts", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidatorTests(unittest.TestCase):
    def test_library_is_valid(self) -> None:
        packs = sorted((MODULE_PATH.parents[1] / "packs").rglob("*.md"))
        self.assertGreaterEqual(len(packs), 14)
        for pack in packs:
            self.assertEqual([], VALIDATOR.validate_file(pack), pack)

    def test_private_path_is_rejected(self) -> None:
        content = "\n".join(["---", "id: test.bad", "---", *VALIDATOR.REQUIRED,
                             "```text", r"Inspect C:\Users\private\notes", "```"])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.md"
            path.write_text(content, encoding="utf-8")
            self.assertIn("publication-hygiene match: windows_user_path",
                          VALIDATOR.validate_file(path))

    def test_impersonation_language_is_rejected(self) -> None:
        content = "\n".join(["---", "id: test.bad-voice", "---", *VALIDATOR.REQUIRED,
                             "```text", "Write exactly in my voice.", "```"])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.md"
            path.write_text(content, encoding="utf-8")
            self.assertIn("publication-hygiene match: impersonation_claim",
                          VALIDATOR.validate_file(path))


if __name__ == "__main__":
    unittest.main()
