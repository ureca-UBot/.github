from __future__ import annotations

import copy
import subprocess
import sys
import unittest
from pathlib import Path

PRODUCT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRODUCT / "scripts"))
import docs_tool as dt  # noqa: E402


class DocsModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = dt.load_yaml(PRODUCT / "data/product.yaml")
        cls.releases = dt.load_yaml(PRODUCT / "docs/releases/product-versions.yaml")
        cls.claims = dt.load_yaml(PRODUCT / "docs/proof/claims.yaml")
        cls.manifest = dt.load_yaml(PRODUCT / "generated/MANIFEST.yaml")

    def check(self, product=None, releases=None, claims=None, manifest=None, mode="template"):
        return dt.validate_model(product or self.product, releases or self.releases,
                                 claims or self.claims, manifest or self.manifest, mode)

    def test_unconfigured_baseline_is_truthfully_unverified_and_template_valid(self):
        self.assertEqual(self.check(), [])
        profile = self.releases["profiles"]["development-preview"]
        self.assertEqual(profile["verification"]["contract_tests"]["status"], "NOT_EVALUATED")
        self.assertEqual(profile["verification"]["product_e2e"]["status"], "NOT_EVALUATED")
        self.assertNotEqual(profile["propagation"]["status"], "VERIFIED")

    def test_missing_component_repo_reference_is_rejected(self):
        product = copy.deepcopy(self.product)
        product["components"]["backend"]["repositories"].append("missing_repo")
        self.assertTrue(any("unknown repository" in e for e in self.check(product=product)))

    def test_artifact_repo_must_belong_to_component(self):
        product = copy.deepcopy(self.product)
        product["artifacts"]["backend_service"]["repository"] = "frontend_repo"
        self.assertTrue(any("not associated" in e for e in self.check(product=product)))

    def test_missing_release_artifact_is_rejected(self):
        releases = copy.deepcopy(self.releases)
        del releases["profiles"]["development-preview"]["artifact_versions"]["backend_service"]
        self.assertTrue(any("missing artifacts" in e for e in self.check(releases=releases)))

    def test_claim_with_nonexistent_evidence_document_is_rejected(self):
        claims = copy.deepcopy(self.claims)
        claims["claims"][0]["evidence"]["document"] = "docs/performance/no-such-file.md"
        self.assertTrue(any("evidence document missing" in e for e in self.check(claims=claims)))

    def test_bogus_pass_status_without_evidence_is_rejected(self):
        releases = copy.deepcopy(self.releases)
        releases["profiles"]["development-preview"]["verification"]["product_e2e"]["status"] = "PASS"
        self.assertTrue(any("PASS requires evidence" in e for e in self.check(releases=releases)))

    def test_supported_profile_requires_product_e2e_and_propagation(self):
        releases = copy.deepcopy(self.releases)
        releases["profiles"]["development-preview"]["production_eligibility"] = "SUPPORTED"
        problems = self.check(releases=releases)
        self.assertTrue(any("cannot be SUPPORTED" in e for e in problems))

    def test_generated_manifest_requires_revision_and_generator(self):
        manifest = {"schema_version": 1, "artifacts": [{
            "status": "GENERATED", "source": {"repository_id": "backend_repo", "path": "openapi.yaml", "commit": "latest"},
            "destination": "generated/api", "consumed_by_profile": "development-preview", "generated_at": None,
            "generator": {"name": "tool", "version": None, "command": "run"},
        }]}
        errors = self.check(manifest=manifest)
        self.assertTrue(any("40-character git SHA" in e for e in errors))
        self.assertTrue(any("generator missing version" in e for e in errors))

    def test_publish_mode_blocks_scaffolding(self):
        problems = self.check(mode="publish")
        self.assertTrue(any("publication_status" in e for e in problems))
        self.assertTrue(any("recommended_profile" in e for e in problems))

    def test_generated_views_are_in_sync(self):
        views = dt.canonical_views(self.product, self.releases, self.claims)
        self.assertEqual(dt.perform_generation(views, True), [])

    def test_markdown_local_links_are_valid(self):
        self.assertEqual(dt.markdown_link_errors("template"), [])

    def test_publish_command_fails_for_unconfigured_template(self):
        result = subprocess.run(
            [sys.executable, "scripts/docs_tool.py", "validate", "--mode", "publish"],
            cwd=PRODUCT, capture_output=True, text=True, check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Publish blocked", result.stderr)
        self.assertIn("CODEOWNERS", result.stderr)


    def test_verified_propagation_requires_matching_desired_observed(self):
        releases = copy.deepcopy(self.releases)
        prop = releases["profiles"]["development-preview"]["propagation"]
        prop.update({
            "status": "VERIFIED", "desired_revision": "release-A",
            "observed_revision": "release-B", "evidence": "https://example.test/evidence",
            "verified_at": "2026-10-26", "environment": "staging"})
        errors = self.check(releases=releases)
        self.assertTrue(any("divergent desired/observed" in e for e in errors))

    def test_conditional_support_requires_declared_conditions_and_checks(self):
        releases = copy.deepcopy(self.releases)
        releases["profiles"]["development-preview"]["production_eligibility"] = "CONDITIONAL"
        errors = self.check(releases=releases)
        self.assertTrue(any("support_conditions" in e for e in errors))
        self.assertTrue(any("cannot be SUPPORTED" in e for e in errors))

    def test_deliberately_broken_link_is_detected(self):
        temp = PRODUCT / "docs" / "overview" / "_validator-test-link.md"
        try:
            temp.write_text('---\ntitle: Test\ntype: test\nstatus: draft\nowner: test\n---\n\n[broken](no-such-target.md)\n', encoding="utf-8")
            errors = dt.markdown_link_errors("template")
            self.assertTrue(any("broken local link" in e for e in errors))
        finally:
            temp.unlink(missing_ok=True)

    def test_generated_view_staleness_is_detected(self):
        views = dt.canonical_views(self.product, self.releases, self.claims)
        modified = dict(views)
        key = next(iter(modified))
        modified[key] = modified[key] + "\nSTALE\n"
        self.assertTrue(any("generated view is stale" in e for e in dt.perform_generation(modified, True)))


class VerifiedExampleTest(unittest.TestCase):
    def test_expected_output_is_asserted(self):
        result = subprocess.run(
            [sys.executable, "examples/verified_example.py", '{"items":[1,2,3]}'],
            cwd=PRODUCT, capture_output=True, text=True, check=True)
        expected = (PRODUCT / "examples/verified-example.expected").read_text(encoding="utf-8")
        self.assertEqual(result.stdout, expected)


if __name__ == "__main__":
    unittest.main()
