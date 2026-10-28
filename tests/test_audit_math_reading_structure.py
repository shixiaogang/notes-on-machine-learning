"""Regression checks for reading structure and scoped label retirement."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/audit_math_reading_structure.py"
SPEC = importlib.util.spec_from_file_location("audit_math_reading_structure", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class CurrentChapterStructureTests(unittest.TestCase):
    def test_part_outlines_keep_volume_local_and_historical_numbers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for volume, folder in enumerate(AUDIT.OUTLINE_DIRECTORIES, 1):
                (root / folder).mkdir(parents=True)
                for part in range(1, 4):
                    title = f"卷{volume}部分{part}"
                    (root / folder / f"{part:02d}-part.md").write_text(
                        f"# {title}\n## 第{part}章 {title}\n"
                        f"### {part}.1 本章小结\n\n说明本章得到的结论。\n"
                    )
            paths, text = AUDIT.reading_structure(root)
            self.assertEqual(len(paths), 15)
            headings = AUDIT.outline_headings(text)
            self.assertEqual(list(headings), [1, 2, 3, 25, 26, 27, 28, 29, 30, 37, 38, 39, 41, 42, 43])
            self.assertEqual(headings[25][1]["number"], "1.1")
            # A volume may carry any number of part outlines; none is required to equal another.
            (root / paths[-1]).unlink()
            self.assertEqual(len(AUDIT.reading_structure(root)[0]), 14)

    def test_current_chapter_numbers_include_nested_titles(self):
        headings = AUDIT.outline_headings(
            "## 第8章 信号的表示与计算\n"
            "### 8.1 信号的表示\n"
            "#### 8.1.1 有限表示\n"
            "##### 8.1.1.1 变换\n"
            "###### 8.1.1.1.1 条件\n"
            "## 第9章 图的表示与计算\n"
            "### 9.1 关系结构\n"
        )
        self.assertEqual(list(headings), [8, 9])
        self.assertEqual([item["level"] for item in headings[8]], [1, 2, 3, 4, 5])
        self.assertEqual(headings[9][1]["number"], "9.1")

    def test_outline_includes_unnumbered_paragraphs_at_their_actual_level(self):
        headings = AUDIT.outline_headings(
            "## 第2章 概率分布\n"
            "### 2.1 信息量\n"
            "#### 2.1.1 连续记录\n"
            "###### 段：微分熵\n"
        )
        self.assertEqual(headings[2][-1]["level"], 5)
        self.assertEqual(headings[2][-1]["title"], "微分熵")

    def test_chapter_map_rejects_duplicate_current_numbers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / AUDIT.CONTRACT).parent.mkdir(parents=True)
            rows = [f"| {n} | 章节{n} | part/chapter{n}.tex |" for n in range(1, 18)]
            (root / AUDIT.CONTRACT).write_text("\n".join(rows))
            self.assertEqual([row["chapter"] for row in AUDIT.assignments(root)], list(range(1, 18)))
            rows[-1] = "| 16 | 章节17 | part/chapter17.tex |"
            (root / AUDIT.CONTRACT).write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "current numbers"):
                AUDIT.assignments(root)

    def current_assignment_rows(self):
        rows = []
        for local, identity in enumerate(
            [1, 2, 3, 5, 22, 23, 24, 18, 21, 4, 27, 28, 29, 30, 31,
             25, 26, 6, 7, 8, 9, 32, 33, 34, 35], 1
        ):
            rows.append(f"| {identity} | 1 | {local} | 章节{identity} | tex/upper/chapter{local}.tex |")
        for local, identity in enumerate([10, 11, 19, 20, 12, 13, 14, 15, 16, 17], 1):
            source = (
                "tex/lower/01-mathematics-and-future-research.tex"
                if identity == 17 else f"tex/lower/chapter{local}.tex"
            )
            rows.append(f"| {identity} | 2 | {local} | 章节{identity} | {source} |")
        return rows

    def test_split_chapters_keep_historical_identities_and_current_positions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / AUDIT.CONTRACT
            path.parent.mkdir(parents=True)
            path.write_text("\n".join(self.current_assignment_rows()))
            rows = AUDIT.assignments(root)
            by_identity = {row["chapter"]: row for row in rows}
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[3]), 3)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[18]), 8)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[21]), 9)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[4]), 10)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[22]), 5)
            self.assertEqual(by_identity[22]["local_chapter"], 5)
            self.assertEqual(by_identity[22]["volume"], 1)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[23]), 6)
            self.assertEqual(by_identity[23]["local_chapter"], 6)
            self.assertEqual(by_identity[23]["volume"], 1)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[24]), 7)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[25]), 16)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[26]), 17)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[32]), 22)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[35]), 25)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[19]), 28)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[20]), 29)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[12]), 30)
            self.assertEqual(AUDIT.current_outline_chapter(by_identity[17]), 35)
            self.assertEqual(by_identity[17]["local_chapter"], 10)
            self.assertEqual(by_identity[17]["volume"], 2)
            self.assertEqual(AUDIT.chapter17_retirement_source(rows), by_identity[17]["path"])

    def test_current_chapter_map_rejects_missing_duplicate_and_reordered_chapters(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / AUDIT.CONTRACT
            path.parent.mkdir(parents=True)
            rows = self.current_assignment_rows()
            path.write_text("\n".join(rows[:-1]))
            with self.assertRaisesRegex(ValueError, "Expected 35 assignments"):
                AUDIT.assignments(root)
            rows[-1] = rows[-1].replace("| 17 |", "| 16 |", 1)
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "exactly once"):
                AUDIT.assignments(root)
            rows = self.current_assignment_rows()
            rows[3] = rows[3].replace("| 1 | 4 |", "| 1 | 3 |", 1)
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "Volume 1 assignments"):
                AUDIT.assignments(root)
            rows = self.current_assignment_rows()
            rows[3], rows[4] = rows[4], rows[3]
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "reading order"):
                AUDIT.assignments(root)

    def test_current_chapter_map_rejects_duplicate_sources_and_mixed_formats(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / AUDIT.CONTRACT
            path.parent.mkdir(parents=True)
            rows = self.current_assignment_rows()
            rows[-2] = rows[-2].replace("chapter9.tex", "chapter8.tex")
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "unique source paths"):
                AUDIT.assignments(root)
            rows = self.current_assignment_rows()
            rows.append("| 21 | 历史格式 | part/legacy.tex |")
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "must not mix"):
                AUDIT.assignments(root)

    def test_current_chapter_map_rejects_duplicate_and_reordered_lower_chapters(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / AUDIT.CONTRACT
            path.parent.mkdir(parents=True)
            rows = self.current_assignment_rows()
            rows[27] = rows[27].replace("| 2 | 3 |", "| 2 | 2 |")
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "Volume 2 assignments"):
                AUDIT.assignments(root)
            rows = self.current_assignment_rows()
            rows[27], rows[28] = rows[28], rows[27]
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "Volume 2 assignments"):
                AUDIT.assignments(root)

    def test_retirement_source_rejects_reassigned_historical_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / AUDIT.CONTRACT
            path.parent.mkdir(parents=True)
            rows = self.current_assignment_rows()
            rows[-1] = rows[-1].replace("| 17 |", "| 15 |", 1)
            rows[-3] = rows[-3].replace("| 15 |", "| 17 |", 1)
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "Historical chapter 17"):
                AUDIT.chapter17_retirement_source(AUDIT.assignments(root))

    def test_chapter_map_accepts_new_chapters_without_renumbering_retirement_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / AUDIT.CONTRACT).parent.mkdir(parents=True)
            rows = self.current_assignment_rows()
            (root / AUDIT.CONTRACT).write_text("\n".join(rows))
            assignments = AUDIT.assignments(root)
            self.assertEqual(len(assignments), 35)
            self.assertEqual(sorted(row["chapter"] for row in assignments), list(range(1, 36)))
            self.assertEqual(
                AUDIT.chapter17_retirement_source(assignments),
                "tex/lower/01-mathematics-and-future-research.tex",
            )

    def test_legacy_format_still_requires_seventeen_historical_chapters(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / AUDIT.CONTRACT
            path.parent.mkdir(parents=True)
            rows = [f"| {n} | 章节{n} | part/chapter{n}.tex |" for n in range(1, 20)]
            path.write_text("\n".join(rows))
            with self.assertRaisesRegex(ValueError, "Expected 17 assignments"):
                AUDIT.assignments(root)


    def test_chapter_audit_follows_nested_inputs_and_keeps_their_labels(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "chapter.tex").write_text(
                "\\chapter{合章}\\label{chap:merged}\n"
                "% \\input{not-active}\n\\input{section}\n"
                "\\section{本章小结}\n"
            )
            (root / "section.tex").write_text(
                "\\section{极限}\\label{sec:limits}\n\\input{detail}\n"
            )
            (root / "detail.tex").write_text("\\subsection{序列}\\label{def:sequence}\n")
            row = {"chapter": 3, "path": "chapter.tex", "title": "合章"}
            expected = AUDIT.outline_headings(
                "## 第3章 合章\n### 3.1 极限\n#### 3.1.1 序列\n### 3.2 本章小结\n"
            )[3]
            report = AUDIT.audit_chapter(root, row, expected)
            self.assertEqual(report["issues"], [])
            self.assertEqual(report["stats"]["labels"], 3)
            (root / "detail.tex").write_text("\\input{section}\n")
            with self.assertRaisesRegex(ValueError, "Recursive chapter input"):
                AUDIT.audit_chapter(root, row, expected)


class Chapter17RetirementTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / AUDIT.RETIRED_LABELS).parent.mkdir(parents=True)
        self.source = "tex/historical-summary/01-mathematics-and-future-research.tex"
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
            locations or {}, {Path("tex/03-foundations/active.tex"): body},
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



class Chapter1RetirementTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / AUDIT.CHAPTER1_RETIRED_LABELS).parent.mkdir(parents=True)
        self.source = str(AUDIT.CHAPTER1_CURRENT_SOURCE)
        self.revision = AUDIT.CHAPTER1_BASELINE_REVISION
        self.old = (
            r"\chapter{旧章}\label{chap:one}" "\n"
            r"\section{集合与关系}\label{eq:kept}" "\n"
            r"\section{命题与证明}\label{eq:old}\label{eq:prior-removal}" "\n"
            r"\section{本章小结}\label{sec:summary}" "\n"
        )
        self.before = (
            r"\chapter{改写前章}\label{chap:one}" "\n"
            r"\section{集合与关系}\label{eq:kept}" "\n"
            r"\section{向量与矩阵}\label{eq:new-kept}" "\n"
            r"\section{命题与证明}\label{eq:old}\label{eq:added}" "\n"
            r"\section{本章小结}\label{sec:summary}" "\n"
        )
        self.baseline = {
            label: str(AUDIT.CHAPTER1_BASELINE_SOURCE)
            for label in AUDIT.LABEL_RE.findall(self.old)
        }
        self.baseline.update({
            "eq:chapter-two": str(AUDIT.CHAPTER2_BASELINE_SOURCE),
            "eq:chapter-seventeen": str(AUDIT.CHAPTER17_BASELINE_SOURCE),
        })
        self.locations = {
            label: [{"path": self.source, "line": 1}]
            for label in ["chap:one", "eq:kept", "eq:new-kept", "sec:summary"]
        }
        inventory = AUDIT.LABEL_RE.findall(self.before)
        self.manifest = {
            "schema_version": 1, "chapter": 1, "source": self.source,
            "baseline_revision": self.revision,
            "baseline_source": str(AUDIT.VOLUME / AUDIT.CHAPTER1_BASELINE_SOURCE),
            "pre_rewrite_revision": AUDIT.CHAPTER1_PRE_REWRITE_REVISION,
            "pre_rewrite_source": str(AUDIT.CHAPTER1_PRE_REWRITE_SOURCE),
            "authorized_baseline_section_titles": ["命题与证明"],
            "authorized_pre_rewrite_section_titles": ["命题与证明"],
            "baseline_source_sha256": AUDIT.hashlib.sha256(self.old.encode()).hexdigest(),
            "pre_rewrite_source_sha256": AUDIT.hashlib.sha256(self.before.encode()).hexdigest(),
            "baseline_section_labels": ["eq:old", "eq:prior-removal"],
            "pre_rewrite_section_labels": ["eq:added", "eq:old"],
            "pre_rewrite_labels": sorted(inventory),
            "pre_rewrite_labels_sha256": AUDIT.label_inventory_sha256(inventory),
            "reason": "User removed only propositions and proofs.",
            "retired_labels": [
                {"label": "eq:old", "present_in": ["baseline", "pre_rewrite"],
                 "reason": "Removed in this revision."},
                {"label": "eq:added", "present_in": ["pre_rewrite"],
                 "reason": "Newer label removed in this revision."},
                {"label": "eq:prior-removal", "present_in": ["baseline"],
                 "reason": "Baseline-only removal, separately identified."},
            ],
        }

    def run_audit(self, body="", locations=None):
        (self.root / AUDIT.CHAPTER1_RETIRED_LABELS).write_text(json.dumps(self.manifest))
        return AUDIT.audit_retired_chapter1_labels(
            self.root, self.revision, self.baseline, self.source,
            self.locations if locations is None else locations,
            {Path("tex/12-systems/active.tex"): AUDIT.uncomment(body)},
            self.old, self.before,
        )

    def kinds(self, result):
        return {issue["kind"] for issue in result["issues"]}

    def test_only_real_topic_labels_are_approved_with_version_provenance(self):
        result = self.run_audit()
        self.assertEqual(result["issues"], [])
        self.assertEqual(result["approved_baseline_retirements"], ["eq:old", "eq:prior-removal"])
        self.assertEqual(result["prior_baseline_only_retirements"], ["eq:prior-removal"])
        self.assertEqual(result["baseline_section_label_count"], 2)
        self.assertEqual(result["pre_rewrite_section_label_count"], 2)

    def test_missing_manifest_never_exempts_labels(self):
        result = AUDIT.audit_retired_chapter1_labels(
            self.root, self.revision, self.baseline, self.source,
            self.locations, {}, self.old, self.before,
        )
        self.assertFalse(result["exists"])
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_unknown_foreign_and_duplicate_entries_fail_closed(self):
        self.manifest["retired_labels"].extend([
            {"label": label, "present_in": [], "reason": "Outside chapter 1."}
            for label in ["eq:chapter-two", "eq:chapter-seventeen", "eq:invented"]
        ] + [dict(self.manifest["retired_labels"][0])])
        result = self.run_audit()
        self.assertIn("retired_label_outside_chapter1_removal_scope", self.kinds(result))
        foreign = [issue["label"] for issue in result["issues"]
                   if issue["kind"] == "foreign_baseline_label_retirement"]
        self.assertEqual(foreign, ["eq:chapter-two", "eq:chapter-seventeen"])
        self.assertIn("duplicate_retired_labels", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_other_sections_and_summary_remain_protected(self):
        for label in ["chap:one", "eq:kept", "eq:new-kept", "sec:summary"]:
            with self.subTest(label=label):
                self.manifest["retired_labels"].append({
                    "label": label, "present_in": [], "reason": "Not an authorized topic.",
                })
                result = self.run_audit(locations={
                    key: value for key, value in self.locations.items() if key != label
                })
                self.assertIn("retired_label_outside_chapter1_removal_scope", self.kinds(result))
                self.assertEqual(result["approved_baseline_retirements"], [])
                self.manifest["retired_labels"].pop()

    def test_unrecorded_removal_elsewhere_in_chapter_is_blocked(self):
        result = self.run_audit(locations={
            key: value for key, value in self.locations.items() if key != "eq:new-kept"
        })
        self.assertIn("unrecorded_chapter1_label_removal", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])
        self.manifest["retired_labels"].pop()
        self.assertIn("unrecorded_chapter1_label_removal", self.kinds(self.run_audit()))

    def test_live_definitions_anywhere_block_retirement(self):
        result = self.run_audit(locations={
            **self.locations, "eq:added": [{"path": "tex/elsewhere.tex", "line": 4}],
        })
        self.assertIn("retired_label_still_defined", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_all_supported_active_reference_forms_block_retirement(self):
        body = r"""\ref{eq:old}
\eqref{eq:added}
\BookSectionRef{eq:old}{fallback}
\hyperref[eq:old]{link}
\cref{eq:unrelated,eq:old}
\crefrange{eq:start}{eq:old}
\getrefnumber{eq:old}
"""
        result = self.run_audit(body)
        refs = [issue for issue in result["issues"]
                if issue["kind"] == "retired_label_active_reference"]
        self.assertEqual(len(refs), 7)
        self.assertEqual(result["approved_baseline_retirements"], [])
        self.assertEqual(self.run_audit(r"% \ref{eq:old}" + "\n")["issues"], [])

    def test_immutable_metadata_inventories_and_provenance_cannot_widen_scope(self):
        for field in ["baseline_revision", "pre_rewrite_revision", "source", "baseline_source",
                      "pre_rewrite_source", "baseline_source_sha256", "pre_rewrite_source_sha256",
                      "authorized_baseline_section_titles", "authorized_pre_rewrite_section_titles",
                      "baseline_section_labels", "pre_rewrite_section_labels", "pre_rewrite_labels",
                      "pre_rewrite_labels_sha256"]:
            with self.subTest(field=field):
                value = self.manifest[field]
                self.manifest[field] = "tampered"
                result = self.run_audit()
                self.assertIn("retirement_manifest_metadata", self.kinds(result))
                self.assertEqual(result["approved_baseline_retirements"], [])
                self.manifest[field] = value
        self.manifest["retired_labels"][1]["present_in"] = ["baseline"]
        self.assertIn("retired_label_source_versions_mismatch", self.kinds(self.run_audit()))

    def test_source_identity_and_authorized_title_are_required(self):
        self.source = "tex/other.tex"
        self.assertIn("chapter1_retirement_identity_mismatch", self.kinds(self.run_audit()))
        self.source = str(AUDIT.CHAPTER1_CURRENT_SOURCE)
        self.revision = "a" * 40
        self.assertIn("chapter1_retirement_identity_mismatch", self.kinds(self.run_audit()))
        self.revision = AUDIT.CHAPTER1_BASELINE_REVISION
        self.before = self.before.replace("命题与证明", "集合与关系")
        result = self.run_audit()
        self.assertIn("chapter1_retirement_scope_missing", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_malformed_entries_and_missing_reasons_fail_closed(self):
        self.manifest["retired_labels"].append("eq:old")
        result = self.run_audit()
        self.assertIn("invalid_retired_label_entry", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])
        self.manifest["retired_labels"].pop()
        self.manifest["retired_labels"][0]["reason"] = " "
        self.manifest["reason"] = " "
        result = self.run_audit()
        self.assertIn("retirement_reason_missing", self.kinds(result))
        self.assertIn("retired_label_reason_missing", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_invalid_json_and_nonobject_manifests_fail_closed(self):
        path = self.root / AUDIT.CHAPTER1_RETIRED_LABELS
        for raw in ["{", "[]"]:
            with self.subTest(raw=raw):
                path.write_text(raw)
                result = AUDIT.audit_retired_chapter1_labels(
                    self.root, self.revision, self.baseline, self.source,
                    self.locations, {}, self.old, self.before,
                )
                self.assertTrue(result["issues"])
                self.assertEqual(result["approved_baseline_retirements"], [])


class Chapter2RetirementTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / AUDIT.CHAPTER2_RETIRED_LABELS).parent.mkdir(parents=True)
        self.source = str(AUDIT.CHAPTER2_CURRENT_SOURCE)
        self.revision = AUDIT.CHAPTER2_BASELINE_REVISION
        self.old = (
            r"\chapter{旧章}\label{chap:two}" "\n"
            r"\section{候选空间的结构与计数}\label{eq:kept}" "\n"
            r"\section{候选空间上的约束与求解}\label{eq:old}" "\n"
            r"\section{问题族的可计算性与复杂度}\label{eq:prior-removal}" "\n"
            r"\section{本章小结}\label{sec:summary}" "\n"
        )
        self.before = (
            r"\chapter{改写前章}\label{chap:two}" "\n"
            r"\section{有限候选的计数}\label{eq:kept}" "\n"
            r"\section{有限输入上的可区分模式}" "\n"
            r"\section{候选解的构造}\label{eq:old}" "\n"
            r"\section{候选解的质量核验}\label{eq:added}" "\n"
            r"\section{问题族的可计算性}" "\n"
            r"\section{问题族的计算复杂度}" "\n"
            r"\section{本章小结}\label{sec:summary}" "\n"
            rf"\label{{{AUDIT.CHAPTER2_SUMMARY_RETIREMENT}}}" "\n"
        )
        self.baseline = {
            label: str(AUDIT.CHAPTER2_BASELINE_SOURCE)
            for label in AUDIT.LABEL_RE.findall(self.old)
        }
        self.baseline["eq:foreign"] = "other-chapter.tex"
        self.locations = {
            label: [{"path": self.source, "line": 1}]
            for label in ["chap:two", "eq:kept", "sec:summary"]
        }
        inventory = AUDIT.LABEL_RE.findall(self.before)
        self.manifest = {
            "schema_version": 1, "chapter": 2, "source": self.source,
            "baseline_revision": self.revision,
            "baseline_source": str(AUDIT.VOLUME / AUDIT.CHAPTER2_BASELINE_SOURCE),
            "pre_rewrite_revision": AUDIT.CHAPTER2_PRE_REWRITE_REVISION,
            "pre_rewrite_source": str(AUDIT.CHAPTER2_PRE_REWRITE_SOURCE),
            "authorized_pre_rewrite_sections": [3, 4, 5, 6],
            "authorized_baseline_section_titles": list(AUDIT.CHAPTER2_BASELINE_SECTION_TITLES),
            "authorized_pre_rewrite_section_titles": list(AUDIT.CHAPTER2_PRE_REWRITE_SECTION_TITLES),
            "authorized_summary_label": AUDIT.CHAPTER2_SUMMARY_RETIREMENT,
            "baseline_source_sha256": AUDIT.hashlib.sha256(self.old.encode()).hexdigest(),
            "pre_rewrite_source_sha256": AUDIT.hashlib.sha256(self.before.encode()).hexdigest(),
            "pre_rewrite_labels": sorted(inventory),
            "pre_rewrite_labels_sha256": AUDIT.label_inventory_sha256(inventory),
            "reason": "User removed former sections 2.3--2.6 and their summary table.",
            "retired_labels": [
                {"label": label, "reason": "Its solving/computability topic was removed."}
                for label in ["eq:old", "eq:prior-removal", "eq:added", AUDIT.CHAPTER2_SUMMARY_RETIREMENT]
            ],
        }

    def run_audit(self, body="", locations=None):
        (self.root / AUDIT.CHAPTER2_RETIRED_LABELS).write_text(json.dumps(self.manifest))
        return AUDIT.audit_retired_chapter2_labels(
            self.root, self.revision, self.baseline, self.source,
            self.locations if locations is None else locations,
            {Path("tex/12-infrastructure/active.tex"): AUDIT.uncomment(body)},
            self.old, self.before,
        )

    def kinds(self, result):
        return {issue["kind"] for issue in result["issues"]}

    def authorize_formula(self):
        label = AUDIT.CHAPTER2_FORMULA_RETIREMENT
        self.old = self.old.replace(r"\label{eq:kept}", rf"\label{{eq:kept}}\label{{{label}}}")
        self.before = self.before.replace(r"\label{eq:kept}", rf"\label{{eq:kept}}\label{{{label}}}")
        self.baseline[label] = str(AUDIT.CHAPTER2_BASELINE_SOURCE)
        self.manifest["baseline_source_sha256"] = AUDIT.hashlib.sha256(self.old.encode()).hexdigest()
        self.manifest["pre_rewrite_source_sha256"] = AUDIT.hashlib.sha256(self.before.encode()).hexdigest()
        inventory = AUDIT.LABEL_RE.findall(self.before)
        self.manifest["pre_rewrite_labels"] = sorted(inventory)
        self.manifest["pre_rewrite_labels_sha256"] = AUDIT.label_inventory_sha256(inventory)
        self.manifest["authorized_formula_labels"] = [label]
        self.manifest["retired_labels"].append({"label": label, "reason": "User removed this formula."})
        return label

    def test_exact_removed_formula_can_be_retired(self):
        label = self.authorize_formula()
        result = self.run_audit()
        self.assertEqual(result["issues"], [])
        self.assertIn(label, result["approved_baseline_retirements"])

    def test_pattern_relocation_requires_live_definition_at_volume_three_destination(self):
        label = "def:pattern"
        self.old = self.old.replace(r"\label{eq:kept}", rf"\label{{eq:kept}}\label{{{label}}}")
        self.before = self.before.replace(
            r"\section{有限输入上的可区分模式}",
            rf"\section{{有限输入上的可区分模式}}\label{{{label}}}",
        )
        self.baseline[label] = str(AUDIT.CHAPTER2_BASELINE_SOURCE)
        self.manifest["baseline_source_sha256"] = AUDIT.hashlib.sha256(self.old.encode()).hexdigest()
        self.manifest["pre_rewrite_source_sha256"] = AUDIT.hashlib.sha256(self.before.encode()).hexdigest()
        inventory = AUDIT.LABEL_RE.findall(self.before)
        self.manifest["pre_rewrite_labels"] = sorted(inventory)
        self.manifest["pre_rewrite_labels_sha256"] = AUDIT.label_inventory_sha256(inventory)
        self.manifest["relocated_pattern_labels"] = [{
            "label": label, "destination": AUDIT.CHAPTER2_PATTERN_DESTINATION,
            "reason": "User moved the full pattern lesson to volume 3.",
        }]
        self.locations[label] = [{"path": AUDIT.CHAPTER2_PATTERN_DESTINATION, "line": 1}]
        result = self.run_audit(body=rf"\ref{{{label}}}")
        self.assertEqual(result["issues"], [])
        self.assertIn(label, result["approved_baseline_relocations"])
        self.locations.pop(label)
        self.assertIn("pattern_relocation_definition", self.kinds(self.run_audit()))
        self.locations[label] = [{"path": "tex/other.tex", "line": 1}]
        self.assertIn("pattern_relocation_definition", self.kinds(self.run_audit()))
        self.manifest["relocated_pattern_labels"][0]["label"] = "eq:kept"
        self.assertIn("pattern_relocation_scope", self.kinds(self.run_audit()))

    def test_formula_scope_cannot_authorize_other_counting_labels(self):
        self.manifest["authorized_formula_labels"] = ["eq:kept"]
        self.manifest["retired_labels"].append({"label": "eq:kept", "reason": "Not authorized."})
        result = self.run_audit()
        self.assertIn("invalid_formula_retirement_scope", self.kinds(result))
        self.assertIn("retired_label_outside_chapter2_removal_scope", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_removed_formula_must_exist_in_both_immutable_sources(self):
        self.manifest["authorized_formula_labels"] = [AUDIT.CHAPTER2_FORMULA_RETIREMENT]
        result = self.run_audit()
        self.assertIn("formula_retirement_source_mismatch", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_removed_formula_cannot_remain_defined_or_referenced(self):
        label = self.authorize_formula()
        result = self.run_audit(body=rf"\eqref{{{label}}}")
        self.assertIn("retired_label_active_reference", self.kinds(result))
        locations = dict(self.locations, **{label: [{"path": self.source, "line": 2}]})
        result = self.run_audit(locations=locations)
        self.assertIn("retired_label_still_defined", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_only_authorized_missing_baseline_labels_are_approved(self):
        result = self.run_audit()
        self.assertEqual(result["issues"], [])
        self.assertEqual(result["approved_baseline_retirements"], ["eq:old", "eq:prior-removal"])
        self.assertNotIn("eq:foreign", result["approved_baseline_retirements"])

    def test_missing_contract_never_exempts_labels(self):
        result = AUDIT.audit_retired_chapter2_labels(
            self.root, self.revision, self.baseline, self.source,
            self.locations, {}, self.old, self.before,
        )
        self.assertFalse(result["exists"])
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_foreign_unknown_and_duplicate_entries_fail_closed(self):
        self.manifest["retired_labels"].extend([
            {"label": "eq:foreign", "reason": "Not chapter 2."},
            {"label": "eq:invented", "reason": "Not in either immutable source."},
            {"label": "eq:old", "reason": "Duplicate."},
        ])
        result = self.run_audit()
        self.assertIn("foreign_baseline_label_retirement", self.kinds(result))
        self.assertIn("retired_label_outside_chapter2_removal_scope", self.kinds(result))
        self.assertIn("duplicate_retired_labels", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])

    def test_counting_and_summary_labels_cannot_be_retired(self):
        for label in ["eq:kept", "sec:summary"]:
            with self.subTest(label=label):
                entry = {"label": label, "reason": "Outside the authorized topics."}
                self.manifest["retired_labels"].append(entry)
                locations = {key: value for key, value in self.locations.items() if key != label}
                result = self.run_audit(locations=locations)
                self.assertIn("retired_label_outside_chapter2_removal_scope", self.kinds(result))
                self.assertEqual(result["approved_baseline_retirements"], [])
                self.manifest["retired_labels"].pop()

    def test_live_definitions_and_cross_volume_references_block_retirement(self):
        result = self.run_audit(locations={**self.locations, "eq:old": [{"path": "another.tex", "line": 5}]})
        self.assertIn("retired_label_still_defined", self.kinds(result))
        for command in [r"\eqref{eq:old}", r"\BookChapterRef{eq:old}{fallback}",
                        r"\hyperref[eq:old]{link}", r"\crefrange{eq:first}{eq:old}"]:
            with self.subTest(command=command):
                result = self.run_audit(command)
                self.assertIn("retired_label_active_reference", self.kinds(result))
                self.assertEqual(result["approved_baseline_retirements"], [])

    def test_immutable_metadata_inventory_and_identity_are_checked(self):
        for field in ["baseline_revision", "pre_rewrite_revision", "source", "baseline_source_sha256"]:
            with self.subTest(field=field):
                old = self.manifest[field]
                self.manifest[field] = "tampered"
                result = self.run_audit()
                self.assertIn("retirement_manifest_metadata", self.kinds(result))
                self.assertEqual(result["approved_baseline_retirements"], [])
                self.manifest[field] = old
        self.manifest["pre_rewrite_labels"].append("eq:invented")
        result = self.run_audit()
        self.assertIn("pre_rewrite_label_inventory_mismatch", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])
        self.revision = "a" * 40
        self.assertIn("chapter2_retirement_identity_mismatch", self.kinds(self.run_audit()))

    def test_unrecorded_removal_and_missing_reason_fail_closed(self):
        removed = self.manifest["retired_labels"].pop()
        result = self.run_audit()
        self.assertIn("unrecorded_chapter2_label_removal", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])
        self.manifest["retired_labels"].append({**removed, "reason": " "})
        result = self.run_audit()
        self.assertIn("retired_label_reason_missing", self.kinds(result))
        self.assertEqual(result["approved_baseline_retirements"], [])


if __name__ == "__main__":
    unittest.main()


class WholeChapterDeletionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.snapshot = r'\chapter{Deleted}\label{chap:deleted}\label{eq:deleted}'
        self.baseline = {'chap:deleted': str(AUDIT.CHAPTER17_BASELINE_SOURCE),
                         'eq:deleted': str(AUDIT.CHAPTER17_BASELINE_SOURCE)}
        self.manifest = {
            'disposition': 'delete-entire-chapter', 'chapter': 17,
            'source_revision': AUDIT.CHAPTER17_DELETION_REVISION,
            'source': AUDIT.CHAPTER17_DELETION_SOURCE,
            'source_sha256': AUDIT.hashlib.sha256(self.snapshot.encode()).hexdigest(),
            'source_labels': ['chap:deleted', 'eq:deleted'],
            'baseline_labels': ['chap:deleted', 'eq:deleted'],
            'authorization': 'Explicit deletion request.',
        }
        (self.root / AUDIT.CHAPTER17_DELETION).parent.mkdir(parents=True)

    def run_audit(self, locations=None, body=''):
        (self.root / AUDIT.CHAPTER17_DELETION).write_text(json.dumps(self.manifest))
        return AUDIT.audit_deleted_chapter17(
            self.root, self.baseline, locations or {}, {Path('live.tex'): body}, self.snapshot,
        )

    def test_explicit_whole_chapter_deletion_requires_exact_snapshot(self):
        result = self.run_audit()
        self.assertEqual(result['issues'], [])
        self.assertEqual(result['approved_baseline_retirements'], ['chap:deleted', 'eq:deleted'])
        self.manifest['source_labels'].remove('eq:deleted')
        result = self.run_audit()
        self.assertEqual(result['approved_baseline_retirements'], [])
        self.assertIn('chapter_deletion_metadata', {issue['kind'] for issue in result['issues']})

    def test_deleted_labels_must_not_remain_defined_or_referenced(self):
        result = self.run_audit({'eq:deleted': [{'path': 'live.tex'}]}, r'\BookChapterRef{chap:deleted}{fallback}')
        self.assertEqual(result['approved_baseline_retirements'], [])
        self.assertEqual({issue['kind'] for issue in result['issues']},
                         {'deleted_chapter_label_still_defined', 'deleted_chapter_active_reference'})

    def test_missing_authorization_never_retires_chapter_labels(self):
        del self.manifest['authorization']
        result = self.run_audit()
        self.assertEqual(result['approved_baseline_retirements'], [])
        self.assertIn('chapter_deletion_authorization_missing', {issue['kind'] for issue in result['issues']})


class FiveVolumeMigrationMapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / AUDIT.CONTRACT
        self.path.parent.mkdir(parents=True)
        self.rows = (SCRIPT.parents[1] / AUDIT.CONTRACT).read_text()

    def test_migrated_map_preserves_identities_and_volume_local_numbers(self):
        self.path.write_text(self.rows)
        rows = AUDIT.assignments(self.root)
        self.assertEqual(len(rows), 43)
        self.assertEqual({row['chapter'] for row in rows}, set(range(1, 46)) - {17, 37})
        self.assertEqual([AUDIT.current_outline_chapter(row) for row in rows], list(range(1, 44)))
        for volume, count in {1: 24, 2: 3, 3: 9, 4: 4, 5: 3}.items():
            self.assertEqual([row['local_chapter'] for row in rows if row['volume'] == volume], list(range(1, count + 1)))

    def test_migrated_map_rejects_missing_identity_and_noncontiguous_local_number(self):
        lines = self.rows.splitlines()
        body = [i for i, line in enumerate(lines) if line.startswith('| ') and line.split('|')[1].strip().isdigit()]
        changed = lines.copy()
        del changed[body[-1]]
        self.path.write_text('\n'.join(changed))
        with self.assertRaisesRegex(ValueError, 'Expected 43 assignments'):
            AUDIT.assignments(self.root)
        changed = lines.copy()
        changed[body[-1]] = changed[body[-1]].replace('| 5 | 3 |', '| 5 | 2 |')
        self.path.write_text('\n'.join(changed))
        with self.assertRaisesRegex(ValueError, 'Volume 5 assignments'):
            AUDIT.assignments(self.root)
