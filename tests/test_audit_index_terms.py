from __future__ import annotations

import importlib.util
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_index_terms.py"


def load_audit_module():
    if not SCRIPT.is_file():
        raise AssertionError(f"missing implementation: {SCRIPT}")
    spec = importlib.util.spec_from_file_location("audit_index_terms", SCRIPT)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot load implementation: {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ScanTexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit_index_terms = load_audit_module()

    def scan(self, text: str):
        return self.audit_index_terms.scan_tex(
            text, Path("tex/01-foundations/chapter.tex"), "01-foundations"
        )

    def test_preserves_optional_sort_key_nested_braces_and_raw_call(self) -> None:
        source = r"前文 \term[k近邻]{$k$\textbf{近{邻}}} 后文"

        occurrence = self.scan(source)[0]

        self.assertEqual(occurrence.raw_sort, "k近邻")
        self.assertEqual(occurrence.raw_display, r"$k$\textbf{近{邻}}")
        self.assertEqual(
            occurrence.raw_call, r"\term[k近邻]{$k$\textbf{近{邻}}}"
        )
        self.assertEqual(occurrence.key, r"$k$\textbf{近{邻}}")
        self.assertEqual((occurrence.line, occurrence.column), (1, 4))

    def test_handles_multiline_arguments_comments_and_exact_location(self) -> None:
        source = textwrap.dedent(
            r"""
              前文
                \term% 参数前注释
                [排序%
                 键]{
                  跨行{词条}
                }
            """
        ).lstrip("\n")

        occurrence = self.scan(source)[0]

        self.assertEqual((occurrence.line, occurrence.column), (2, 3))
        self.assertEqual(occurrence.raw_sort, "排序%\n   键")
        self.assertEqual(occurrence.key, "跨行{词条}")
        self.assertIn("% 参数前注释", occurrence.raw_call)

    def test_distinguishes_escaped_percent_braces_and_comment_percent(self) -> None:
        source = (
            "\\term{百分比\\%与\\{花括号\\}} "
            "\\\\% \\term{注释中伪调用}\n"
            "\\term{保留}"
        )

        occurrences = self.scan(source)

        self.assertEqual(
            [item.key for item in occurrences],
            [r"百分比\%与\{花括号\}", "保留"],
        )
        self.assertEqual((occurrences[1].line, occurrences[1].column), (2, 1))

    def test_skips_comments_verbatim_environments_and_verb_commands(self) -> None:
        source = textwrap.dedent(
            r"""
            % \term{注释}
            \begin{verbatim}
            \term{verbatim}
            \end{verbatim}
            \begin{Verbatim}\term{Verbatim}\end{Verbatim}
            \begin{lstlisting}\term{listing}\end{lstlisting}
            \begin{minted}{tex}\term{minted}\end{minted}
            \verb|\term{verb}| \verb*+\term{verb-star}+
            \terminal{不是 term}\term{真实词条}
            """
        )

        occurrences = self.scan(source)

        self.assertEqual([item.key for item in occurrences], ["真实词条"])

    def test_extracts_only_adjacent_english_parenthetical_candidate(self) -> None:
        source = (
            r"\term{支持向量机}（support vector machine, SVM）"
            r"\term{无候选}正文（later English）"
        )

        occurrences = self.scan(source)

        self.assertEqual(occurrences[0].candidate, "support vector machine")
        self.assertEqual(occurrences[0].abbreviation, "SVM")
        self.assertIsNone(occurrences[1].candidate)

    def test_scans_semantic_alias_as_display_occurrence(self) -> None:
        source = r"\termalias{pgm-soundness}{可靠性}（soundness）"

        occurrences = self.scan(source)

        self.assertEqual([item.key for item in occurrences], ["可靠性"])
        self.assertEqual(occurrences[0].semantic_id, "pgm-soundness")
        self.assertEqual(occurrences[0].candidate, "soundness")

    def test_ignores_bare_input_control_word_used_as_a_variable(self) -> None:
        source = r"\foreach \input in {a,b} {$\input$}\term{真实词条}"

        occurrences = self.scan(source)

        self.assertEqual([item.key for item in occurrences], ["真实词条"])

    def test_reports_unclosed_optional_argument_at_term_position(self) -> None:
        with self.assertRaisesRegex(
            self.audit_index_terms.ScanError,
            r"chapter\.tex:1:1: unclosed optional argument",
        ):
            self.scan(r"\term[排序键{词条}")

    def test_reports_unclosed_required_argument_at_term_position(self) -> None:
        with self.assertRaisesRegex(
            self.audit_index_terms.ScanError,
            r"chapter\.tex:2:3: unclosed required argument",
        ):
            self.scan("前文\n  \\term{未闭合")


class CollectTermsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit_index_terms = load_audit_module()

    def test_follows_input_order_and_assigns_shared_terms_to_first_volume(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            volumes = [
                "01-foundations",
                "02-models",
                "03-paradigms",
                "04-applications",
                "05-systems",
            ]
            for volume in volumes:
                volume_dir = root / "tex" / volume
                volume_dir.mkdir(parents=True)
                (volume_dir / "volume.tex").write_text("", encoding="utf-8")
            first = root / "tex" / "01-foundations"
            (first / "volume.tex").write_text(
                "\\input{fragments/root}\n"
                "\\input{tex/01-foundations/b}\n"
                "\\input{tex/01-foundations/a}\n",
                encoding="utf-8",
            )
            fragments = root / "fragments"
            fragments.mkdir()
            (fragments / "root.tex").write_text(
                "\\term{根目录输入}", encoding="utf-8"
            )
            (first / "a.tex").write_text(
                "\\term{甲}\\term{共享}", encoding="utf-8"
            )
            (first / "b.tex").write_text(
                "\\term{乙}\\input{tex/01-foundations/nested}", encoding="utf-8"
            )
            (first / "nested.tex").write_text(
                "\\term{共享}\\term{丙}", encoding="utf-8"
            )
            styles = root / "tex" / "styles"
            styles.mkdir()
            (styles / "environments.tex").write_text(
                "\\newcommand{\\InputLabel}{\\term{输入：}}\n"
                "\\newcommand{\\OutputLabel}{\\term{输出：}}\n",
                encoding="utf-8",
            )

            occurrences = self.audit_index_terms.collect_terms(root)

        self.assertEqual(
            [item.key for item in occurrences],
            [
                "根目录输入",
                "乙",
                "共享",
                "丙",
                "甲",
                "共享",
                "输入：",
                "输出：",
            ],
        )
        self.assertTrue(
            all(item.volume == "01-foundations" for item in occurrences)
        )


class MappingAndAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit_index_terms = load_audit_module()

    def occurrence(
        self,
        display: str,
        volume: str = "01-foundations",
        sort_key: str | None = None,
    ):
        optional = f"[{sort_key}]" if sort_key is not None else ""
        return self.audit_index_terms.TermOccurrence(
            path=Path(f"tex/{volume}/chapter.tex"),
            volume=volume,
            line=1,
            column=1,
            raw_call=f"\\term{optional}{{{display}}}",
            raw_display=display,
            raw_sort=sort_key,
            key=display,
            sort_key=sort_key or display,
        )

    def mapping(
        self,
        source: str,
        translation: str,
        owner: str = "01-foundations",
        line: int = 1,
    ):
        return self.audit_index_terms.TermMapping(
            path=Path(f"tex/index-terms/{owner}.tex"),
            owner=owner,
            line=line,
            column=1,
            raw_source=source,
            raw_translation=translation,
            key=source,
            translation=translation,
        )

    def test_parses_balanced_mapping_arguments_and_owner(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shard = root / "tex" / "index-terms" / "01-foundations.tex"
            shard.parent.mkdir(parents=True)
            shard.write_text(
                "\\DeclareBookIndexTerm"
                "{含{嵌套}词条}"
                "{nested {English} term}\n",
                encoding="utf-8",
            )

            mappings = self.audit_index_terms.parse_mappings(root)

        self.assertEqual(len(mappings), 1)
        self.assertEqual(mappings[0].key, "含{嵌套}词条")
        self.assertEqual(mappings[0].translation, "nested {English} term")
        self.assertEqual(mappings[0].owner, "01-foundations")

    def test_parses_semantic_alias_separately_from_base_mappings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shard = root / "tex" / "index-terms" / "01-foundations.tex"
            shard.parent.mkdir(parents=True)
            shard.write_text(
                "% \\DeclareBookIndexTermAlias"
                "{commented}{注释}{commented}\n"
                "\\begin{verbatim}\n"
                "\\DeclareBookIndexTermAlias"
                "{verbatim}{原样}{verbatim}\n"
                "\\end{verbatim}\n"
                "\\DeclareBookIndexTerm{可靠性}{reliability}\n"
                "\\DeclareBookIndexTermAlias"
                "{pgm-soundness}{可靠性}{soundness}\n",
                encoding="utf-8",
            )

            mappings = self.audit_index_terms.parse_mappings(root)
            aliases = self.audit_index_terms.parse_aliases(root)

        self.assertEqual(len(mappings), 1)
        self.assertEqual(len(aliases), 1)
        self.assertEqual(aliases[0].identity, "pgm-soundness")
        self.assertEqual(aliases[0].display, "可靠性")
        self.assertEqual(aliases[0].translation, "soundness")

    def test_repository_expands_njw_and_geglu_accurately(self) -> None:
        mappings = {
            mapping.key: mapping.translation
            for mapping in self.audit_index_terms.parse_mappings(ROOT)
        }

        self.assertEqual(
            mappings["NJW 算法"], "Ng--Jordan--Weiss algorithm"
        )
        self.assertEqual(
            mappings["GEGLU"], "GELU-gated linear unit"
        )

    def test_audit_accepts_declared_alias_without_changing_base_coverage(
        self,
    ) -> None:
        base = self.occurrence("可靠性")
        alias = self.occurrence("可靠性")
        alias = alias._replace(
            raw_call=r"\termalias{pgm-soundness}{可靠性}",
            sort_key="可靠性-pgm-soundness",
            semantic_id="pgm-soundness",
        )
        aliases = [
            self.audit_index_terms.TermAlias(
                path=Path("tex/index-terms/01-foundations.tex"),
                owner="01-foundations",
                line=2,
                column=1,
                raw_identity="pgm-soundness",
                raw_display="可靠性",
                raw_translation="soundness",
                identity="pgm-soundness",
                display="可靠性",
                translation="soundness",
            )
        ]

        diagnostics = self.audit_index_terms.audit(
            [base, alias],
            [self.mapping("可靠性", "reliability")],
            aliases,
        )

        self.assertEqual(diagnostics, [])

    def test_audit_reports_all_mapping_integrity_failures(self) -> None:
        occurrences = [
            self.occurrence("中文缺失"),
            self.occurrence("SVM"),
            self.occurrence("重复"),
            self.occurrence("排序冲突", sort_key="甲"),
            self.occurrence("排序冲突", sort_key="乙"),
        ]
        mappings = [
            self.mapping("SVM", ""),
            self.mapping("重复", "duplicate"),
            self.mapping("重复", "conflict", line=2),
            self.mapping("孤立", "orphan"),
            self.mapping("自映射", "自映射"),
            self.mapping("错误分片", "wrong owner", owner="02-models"),
        ]
        occurrences.append(self.occurrence("错误分片"))

        diagnostics = self.audit_index_terms.audit(occurrences, mappings)
        codes = [diagnostic.code for diagnostic in diagnostics]

        self.assertIn("MISSING_MAPPING", codes)
        self.assertIn("MISSING_ABBREVIATION_EXPANSION", codes)
        self.assertIn("EMPTY_TRANSLATION", codes)
        self.assertIn("DUPLICATE_MAPPING", codes)
        self.assertIn("TRANSLATION_CONFLICT", codes)
        self.assertIn("ORPHAN_MAPPING", codes)
        self.assertIn("SELF_MAPPING", codes)
        self.assertIn("WRONG_OWNER", codes)
        self.assertIn("SORT_KEY_CONFLICT", codes)

    def test_audit_accepts_unmapped_complete_english_name_and_math_term(self) -> None:
        occurrences = [
            self.occurrence("Gaussian process"),
            self.occurrence(r"$R^2$"),
            self.occurrence("ResNet"),
        ]

        diagnostics = self.audit_index_terms.audit(occurrences, [])

        self.assertEqual(diagnostics, [])

    def test_audit_assigns_cross_volume_term_to_global_first_occurrence(self) -> None:
        occurrences = [
            self.occurrence("共享词", volume="02-models"),
            self.occurrence("共享词", volume="03-paradigms"),
        ]
        mappings = [self.mapping("共享词", "shared term", owner="02-models")]

        diagnostics = self.audit_index_terms.audit(occurrences, mappings)

        self.assertEqual(diagnostics, [])

    def test_audit_reports_abbreviation_mapping_cycles(self) -> None:
        occurrences = [
            self.occurrence("ABC"),
            self.occurrence("XYZ"),
        ]
        mappings = [
            self.mapping("ABC", "XYZ"),
            self.mapping("XYZ", "ABC"),
        ]

        diagnostics = self.audit_index_terms.audit(occurrences, mappings)

        self.assertIn(
            "ABBREVIATION_CYCLE",
            [diagnostic.code for diagnostic in diagnostics],
        )

    def test_audit_statistics_reports_call_and_unique_count_drift(self) -> None:
        occurrences = [
            self.occurrence("重复"),
            self.occurrence("重复"),
        ]

        diagnostics = self.audit_index_terms.audit_statistics(
            occurrences, expected_calls=3, expected_unique=2
        )

        self.assertEqual(
            [diagnostic.code for diagnostic in diagnostics],
            ["CALL_COUNT_MISMATCH", "UNIQUE_COUNT_MISMATCH"],
        )

    def test_index_artifact_audit_reports_orphan_english_and_repeated_pages(
        self,
    ) -> None:
        occurrences = [self.occurrence("机器学习")]
        mappings = [self.mapping("机器学习", "machine learning")]
        idx = (
            "\\indexentry{机器学习@机器学习，machine learning|hyperpage}{1}\n"
            "\\indexentry{orphan@machine learning|hyperpage}{2}\n"
            "\\indexentry{机器学习@机器学习，wrong|hyperpage}{3}\n"
        )
        ind = (
            "\\item 机器学习，machine learning，"
            "\\hyperpage{1}，\\hyperpage{1}\n"
        )

        diagnostics = self.audit_index_terms.audit_index_artifacts(
            occurrences, mappings, idx, ind, Path("build/main")
        )
        codes = [diagnostic.code for diagnostic in diagnostics]

        self.assertIn("ORPHAN_INDEX_ENGLISH", codes)
        self.assertIn("INDEX_TRANSLATION_MISMATCH", codes)
        self.assertIn("DUPLICATE_INDEX_PAGE", codes)

    def test_index_artifact_audit_accepts_known_standalone_english_term(
        self,
    ) -> None:
        occurrences = [
            self.occurrence("K均值聚类"),
            self.occurrence("K-means"),
        ]
        mappings = [self.mapping("K均值聚类", "K-means")]
        idx = "\\indexentry{K-means@K-means|hyperpage}{1}\n"

        diagnostics = self.audit_index_terms.audit_index_artifacts(
            occurrences, mappings, idx, "", Path("build/main")
        )

        self.assertEqual(diagnostics, [])

    def test_index_artifact_audit_rejects_untranslated_mapped_term(
        self,
    ) -> None:
        occurrences = [self.occurrence("机器学习")]
        mappings = [self.mapping("机器学习", "machine learning")]
        idx = "\\indexentry{机器学习@机器学习|hyperpage}{1}\n"

        diagnostics = self.audit_index_terms.audit_index_artifacts(
            occurrences, mappings, idx, "", Path("build/main")
        )

        self.assertEqual(
            [diagnostic.code for diagnostic in diagnostics],
            ["MISSING_INDEX_TRANSLATION"],
        )

    def test_index_artifact_audit_rejects_alias_on_default_identity(
        self,
    ) -> None:
        base = self.occurrence("忠实性")
        alias_occurrence = self.occurrence("忠实性")._replace(
            raw_call=r"\termalias{pgm-faithfulness}{忠实性}",
            sort_key="忠实性-pgm-faithfulness",
            semantic_id="pgm-faithfulness",
        )
        alias = self.audit_index_terms.TermAlias(
            path=Path("tex/index-terms/02-models.tex"),
            owner="02-models",
            line=1,
            column=1,
            raw_identity="pgm-faithfulness",
            raw_display="忠实性",
            raw_translation="faithfulness",
            identity="pgm-faithfulness",
            display="忠实性",
            translation="faithfulness",
        )
        idx = "\\indexentry{忠实性@忠实性，faithfulness|hyperpage}{1}\n"

        diagnostics = self.audit_index_terms.audit_index_artifacts(
            [base, alias_occurrence],
            [self.mapping("忠实性", "fidelity")],
            idx,
            "",
            Path("build/main"),
            [alias],
        )

        self.assertEqual(
            [diagnostic.code for diagnostic in diagnostics],
            ["INDEX_TRANSLATION_MISMATCH"],
        )

    def test_index_artifact_audit_rejects_unknown_sort_identity(
        self,
    ) -> None:
        occurrences = [self.occurrence("机器学习")]
        mappings = [self.mapping("机器学习", "machine learning")]
        idx = (
            "\\indexentry{未知身份@机器学习，"
            "machine learning|hyperpage}{1}\n"
        )

        diagnostics = self.audit_index_terms.audit_index_artifacts(
            occurrences, mappings, idx, "", Path("build/main")
        )

        self.assertEqual(
            [diagnostic.code for diagnostic in diagnostics],
            ["INDEX_TRANSLATION_MISMATCH"],
        )

    def test_index_artifact_audit_rejects_wrong_chinese_display(
        self,
    ) -> None:
        occurrences = [
            self.occurrence("机器学习"),
            self.occurrence("深度学习"),
        ]
        mappings = [
            self.mapping("机器学习", "machine learning"),
            self.mapping("深度学习", "deep learning"),
        ]
        idx = (
            "\\indexentry{机器学习@深度学习，"
            "machine learning|hyperpage}{1}\n"
        )

        diagnostics = self.audit_index_terms.audit_index_artifacts(
            occurrences, mappings, idx, "", Path("build/main")
        )

        self.assertEqual(
            [diagnostic.code for diagnostic in diagnostics],
            ["INDEX_TRANSLATION_MISMATCH"],
        )

    def test_index_artifact_audit_normalizes_xetex_math_expansion(
        self,
    ) -> None:
        occurrences = [
            self.occurrence(r"$\epsilon$不敏感损失"),
            self.occurrence(r"$\widehat R$诊断"),
            self.occurrence(r"加权$k$近邻"),
        ]
        mappings = [
            self.mapping(
                r"$\epsilon$不敏感损失",
                r"$\epsilon$-insensitive loss",
            ),
            self.mapping(r"$\widehat R$诊断", "R-hat diagnostic"),
            self.mapping(
                r"加权$k$近邻",
                r"weighted $k$-nearest neighbors",
            ),
        ]
        idx = (
            "\\indexentry{$\\epsilon $不敏感损失@"
            "$\\epsilon $不敏感损失，"
            "$\\epsilon $-insensitive loss|hyperpage}{1}\n"
            "\\indexentry{$\\mathaccent \"019A\\relax R$诊断@"
            "$\\mathaccent \"019A\\relax R$诊断，"
            "R-hat diagnostic|hyperpage}{2}\n"
            "\\indexentry{加权$k $近邻@加权$k $近邻，"
            "weighted $k $-nearest neighbors|hyperpage}{3}\n"
        )

        diagnostics = self.audit_index_terms.audit_index_artifacts(
            occurrences, mappings, idx, "", Path("build/main")
        )

        self.assertEqual(diagnostics, [])

    def test_index_artifact_audit_does_not_match_translation_substrings(
        self,
    ) -> None:
        occurrences = [
            self.occurrence("活跃"),
            self.occurrence("主动学习"),
        ]
        mappings = [
            self.mapping("活跃", "active"),
            self.mapping("主动学习", "active learning"),
        ]
        idx = (
            "\\indexentry{主动学习@主动学习，"
            "active learning|hyperpage}{1}\n"
        )

        diagnostics = self.audit_index_terms.audit_index_artifacts(
            occurrences, mappings, idx, "", Path("build/main")
        )

        self.assertEqual(diagnostics, [])


if __name__ == "__main__":
    unittest.main()
