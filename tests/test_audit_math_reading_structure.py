"""Regression checks for explicit chapter-17 label retirement."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/audit_math_reading_structure.py"
SPEC = importlib.util.spec_from_file_location("audit_math_reading_structure", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class Chapter17RetirementTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "plans").mkdir()
        self.source = "tex/01-mathematical-preliminaries/06-mathematics-and-machine-learning/01-mathematics-and-future-research.tex"
        self.revision = "a" * 40
        self.baseline = {
            "eq:old": str(AUDIT.CHAPTER17_BASELINE_SOURCE),
            "eq:other-chapter": "01-other/01-other.tex",
        }
        self.inventory = ["eq:old", "sec:added-during-restructure"]
        self.manifest = {
            "schema_version": 1, "chapter": 17, "source": self.source,
            "baseline_revision": self.revision,
            "baseline_source": str(AUDIT.VOLUME / AUDIT.CHAPTER17_BASELINE_SOURCE),
            "reason": "Authorized fresh rewrite removes unrelated old material.",
            "pre_rewrite_source_sha256": "b" * 64,
            "pre_rewrite_labels": self.inventory,
            "pre_rewrite_labels_sha256": AUDIT.label_inventory_sha256(self.inventory),
            "retired_labels": [
                {"label": label, "reason": "Removed from the fresh rewrite."}
                for label in self.inventory
            ],
        }

    def run_audit(self, body="", locations=None):
        (self.root / AUDIT.RETIRED_LABELS).write_text(json.dumps(self.manifest))
        return AUDIT.audit_retired_chapter17_labels(
            self.root, self.revision, self.baseline, self.source,
            locations or {}, {Path("tex/02-foundations/active.tex"): body},
        )

    def kinds(self, result):
        return {issue["kind"] for issue in result["issues"]}

    def test_explicit_unreferenced_retirement_only_exempts_chapter17_baseline(self):
        result = self.run_audit()
        self.assertEqual(result["issues"], [])
        self.assertEqual(result["approved_baseline_retirements"], ["eq:old"])

    def test_missing_manifest_does_not_exempt_any_label(self):
        result = AUDIT.audit_retired_chapter17_labels(
            self.root, self.revision, self.baseline, self.source, {}, {},
        )
        self.assertFalse(result["exists"])
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_standard_project_range_and_hyperlink_references_block_retirement(self):
        body = r"""\eqref{eq:old}
\BookSectionRef{eq:old}{A readable fallback}
\hyperref[eq:old]{link}
\cref{eq:unrelated,eq:old}
\crefrange{eq:start}{eq:old}
\getrefnumber{eq:old}
"""
        result = self.run_audit(body)
        refs = [issue for issue in result["issues"] if issue["kind"] == "retired_label_active_reference"]
        self.assertEqual(len(refs), 6)
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_comments_do_not_create_active_references(self):
        body = AUDIT.uncomment(r"% \ref{eq:old}" + "\n" + r"\ref{eq:unrelated}")
        self.assertEqual(self.run_audit(body)["issues"], [])

    def test_retired_label_still_defined_is_a_stale_exception(self):
        result = self.run_audit(locations={"eq:old": [{"path": self.source, "line": 4}]})
        self.assertIn("retired_label_still_defined", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_unrecorded_removal_is_not_silently_allowed(self):
        self.manifest["retired_labels"].pop()
        result = self.run_audit()
        self.assertIn("unrecorded_chapter17_label_removal", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_other_chapter_baseline_cannot_enter_exception_inventory(self):
        self.inventory.append("eq:other-chapter")
        self.manifest["pre_rewrite_labels_sha256"] = AUDIT.label_inventory_sha256(self.inventory)
        self.manifest["retired_labels"].append({"label": "eq:other-chapter", "reason": "Invalid scope."})
        result = self.run_audit()
        self.assertIn("foreign_baseline_labels_in_inventory", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_unknown_labels_and_duplicate_entries_fail_closed(self):
        self.manifest["retired_labels"].extend([
            {"label": "eq:invented", "reason": "Not in the old source."},
            {"label": "eq:old", "reason": "Duplicate."},
        ])
        result = self.run_audit()
        self.assertIn("retired_label_not_in_pre_rewrite_source", self.kinds(result))
        self.assertIn("duplicate_retired_labels", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_changed_baseline_or_fingerprint_does_not_disable_preservation(self):
        self.manifest["baseline_revision"] = "c" * 40
        self.manifest["pre_rewrite_labels_sha256"] = "d" * 64
        result = self.run_audit()
        self.assertIn("retirement_manifest_metadata", self.kinds(result))
        self.assertIn("pre_rewrite_label_inventory_sha256_mismatch", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])


if __name__ == "__main__":
    unittest.main()
