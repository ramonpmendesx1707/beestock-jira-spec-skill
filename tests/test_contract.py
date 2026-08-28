from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "skills" / "criar-especificacao"


class SkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = (PRIMARY / "SKILL.md").read_text(encoding="utf-8")
        cls.interview = (PRIMARY / "references" / "interview.md").read_text(encoding="utf-8")
        cls.audit = (PRIMARY / "references" / "audit-rubric.md").read_text(encoding="utf-8")
        cls.jira = (PRIMARY / "references" / "jira-format.md").read_text(encoding="utf-8")

    def test_default_is_complete_mode(self) -> None:
        self.assertIn("Use `COMPLETO` por padrão", self.skill)

    def test_summary_mode_stops_interview(self) -> None:
        self.assertIn("Pare de expandir a árvore", self.interview)
        self.assertIn("não retorne à sabatina", self.audit)

    def test_summary_mode_never_invents(self) -> None:
        self.assertIn("Nenhuma decisão ou regra foi inventada", self.audit)

    def test_full_mode_has_audit_loop(self) -> None:
        self.assertRegex(self.skill, r"lacunas bloqueantes retornam a `SABATINA`")
        self.assertIn("Completude funcional", self.audit)
        self.assertIn("Clareza, padrão e testabilidade", self.audit)
        self.assertIn("não deve receber nem consultar os arquivos de exemplos", self.audit)

    def test_every_requirement_needs_traceability(self) -> None:
        self.assertIn("Matriz interna de rastreabilidade", self.jira)
        self.assertIn("Frases retiradas apenas de exemplos", self.jira)

    def test_summary_future_points_are_bounded(self) -> None:
        self.assertIn("no máximo 3 itens", self.jira)
        self.assertIn("não integram o escopo confirmado", self.jira)

    def test_business_level_boundary(self) -> None:
        for forbidden_example in ("ajustar o backend", "alterar a query", "criar classe", "salvar na tabela"):
            self.assertIn(forbidden_example, self.jira)
        self.assertIn("Deixe a forma interna de implementação", self.jira)

    def test_new_demands_are_isolated(self) -> None:
        self.assertIn("cada novo tema como um caso independente", self.skill)

    def test_signature_is_exact(self) -> None:
        self.assertIn("Att,\n\nRamon Mendes.", self.skill)

    def test_jira_key_normalization(self) -> None:
        self.assertIn("https://szsolucoes.atlassian.net/browse/BEES-3005", self.jira)

    def test_all_references_are_relative_and_exist(self) -> None:
        targets = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", self.skill)
        self.assertGreater(len(targets), 4)
        for target in targets:
            self.assertTrue((PRIMARY / target).exists(), target)


if __name__ == "__main__":
    unittest.main()
