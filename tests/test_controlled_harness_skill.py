import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = (
    REPO_ROOT / ".github" / "skills" / "controlled-harness-engineering"
)


class ControlledHarnessSkillTests(unittest.TestCase):
    def test_skill_package_contains_required_files(self):
        expected_files = [
            "SKILL.md",
            "LICENSE-HARNESSCODE",
            "references/workflow.md",
            "references/safety-gates.md",
            "references/role-definitions.md",
            "references/state-schema.md",
            "templates/feature-ledger.json",
            "templates/blocker-report.json",
            "templates/verification-report.json",
            "templates/completion-report.md",
        ]

        missing = [
            relative_path
            for relative_path in expected_files
            if not (SKILL_ROOT / relative_path).is_file()
        ]

        self.assertEqual([], missing, f"Missing skill files: {missing}")

    def test_skill_frontmatter_and_references_are_valid(self):
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        frontmatter_match = re.match(r"\A---\n(.*?)\n---\n", skill_text, re.DOTALL)

        self.assertIsNotNone(frontmatter_match, "SKILL.md needs YAML frontmatter")
        frontmatter = frontmatter_match.group(1)
        self.assertIn("name: controlled-harness-engineering", frontmatter)
        self.assertRegex(frontmatter, r"(?m)^description:\s*.+")

        referenced_files = re.findall(
            r"`((?:references|templates)/[^`]+)`", skill_text
        )
        self.assertGreater(len(referenced_files), 0)
        for relative_path in referenced_files:
            self.assertTrue(
                (SKILL_ROOT / relative_path).is_file(),
                f"Referenced file does not exist: {relative_path}",
            )

    def test_json_templates_parse(self):
        for template_name in [
            "feature-ledger.json",
            "blocker-report.json",
            "verification-report.json",
        ]:
            template_path = SKILL_ROOT / "templates" / template_name
            with self.subTest(template=template_name):
                json.loads(template_path.read_text(encoding="utf-8"))

    def test_skill_enforces_controlled_execution(self):
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        safety_text = (
            SKILL_ROOT / "references" / "safety-gates.md"
        ).read_text(encoding="utf-8")
        workflow_text = (
            SKILL_ROOT / "references" / "workflow.md"
        ).read_text(encoding="utf-8")
        combined = "\n".join([skill_text, safety_text, workflow_text]).lower()

        required_rules = [
            "no automatic commits",
            "do not delete useful tests",
            "skipped validation is unresolved",
            "failing test first",
            "fresh verification",
            "worktree",
            "human approval",
        ]
        for rule in required_rules:
            with self.subTest(rule=rule):
                self.assertIn(rule, combined)

    def test_upstream_license_is_preserved(self):
        license_text = (SKILL_ROOT / "LICENSE-HARNESSCODE").read_text(
            encoding="utf-8"
        )

        self.assertIn("MIT License", license_text)
        self.assertIn("Copyright (c) 2026 yzddp", license_text)


if __name__ == "__main__":
    unittest.main()
