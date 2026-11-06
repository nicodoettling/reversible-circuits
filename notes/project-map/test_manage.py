"""Isolated maintenance checks; no research artifacts or sampler runs touched."""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import manage


class MapChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "notes/project-map").mkdir(parents=True)
        (self.root / "research/mission-M01").mkdir(parents=True)
        (self.root / "research/proof.md").write_text("# Frozen Theorem\n\nClaim.\n")
        (self.root / "research/ledger.md").write_text("### L-0001 - Initial\n")
        (self.root / "research/run.log").write_text("started\n")
        source = {"path": "research/proof.md", "read_scope": "fixture only",
                  "checked_locators": ["# Frozen Theorem"],
                  "sha256": manage.digest(self.root / "research/proof.md")}
        prototype = dict(version=1, title="Fixture", kind="theorem", model="global",
                         family="f", claim="Fixture only", parameters="N>=2",
                         guards="nonempty", assumptions="fixture", open_obligations="none",
                         source_claimed_status="accepted", effective_status="accepted-inherited",
                         check_depth="statement-and-verdict-traced", checked="fixture",
                         review_binding="fixture verdict", evidence=["proof"],
                         adjudications=["proof"], limitations="not mathematics", aliases=[],
                         regressions="none", disagreements="none", view="results")
        self.cat = {
            "date": "2026-10-01", "timezone": "UTC", "models": {"global": "fixture"},
            "sources": {"proof": source},
            "records": [{**copy.deepcopy(prototype), "id": rid, "dependencies": deps}
                        for rid, deps in (("A", []), ("B", ["A"]), ("C", ["B"]))],
            "coverage": [{"id": "f", "title": "Fixture", "prefixes": ["research"],
                          "disposition": "pending", "read_depth": "inventory-only",
                          "limits": "fixture", "records": ["A"], "branch_disposition": "pending"}],
            "inventory_policy": {
                "pruned_directory_names": [".git"],
                "excluded_paths": ["notes/project-map", "PROJECT_MAP.md"],
                "excluded_filename_patterns": ["*.aux"], "telemetry_patterns": ["*.log"],
                "branch_heading_sources": ["research/ledger.md"]},
            "relations": [], "targets": [], "briefs": [], "branch_overrides": [],
            "project": {"frontier_paragraphs": ["Fixture only."], "routes": {}},
            "maintenance_commands": [], "coverage_scope": "fixture", "conflicts": []}
        self.baseline = manage.discover(self.root, self.cat)
        (self.root / "notes/project-map/UPDATE_PROTOCOL.md").write_text("# Protocol\n")

    def errors(self):
        return "\n".join(manage.validate(self.root, self.cat))

    def cli(self, *args):
        folder = self.root / "notes/project-map"
        (folder / "catalogue.json").write_text(json.dumps(self.cat))
        (folder / "inventory.json").write_text(json.dumps(self.baseline))
        return subprocess.run([sys.executable, "-B", str(Path(manage.__file__).resolve()),
                               "--root", str(self.root), *args], text=True, capture_output=True)

    def test_valid_fixture(self):
        self.assertEqual(self.errors(), "")

    def test_changed_evidence_reports_transitive_cone(self):
        (self.root / "research/proof.md").write_text("changed")
        self.assertIn("evidence drift", self.errors())
        self.assertIn("A, B, C", self.errors())

    def test_deleted_evidence(self):
        (self.root / "research/proof.md").unlink()
        self.assertIn("evidence drift", self.errors())
        delta = manage.drift(self.baseline, manage.discover(self.root, self.cat))
        self.assertEqual(delta["missing"], ["research/proof.md"])

    def test_new_source_in_old_family(self):
        (self.root / "research/new.md").write_text("new")
        current = manage.discover(self.root, self.cat)
        self.assertEqual(current["files"]["research/new.md"]["family"], "f")
        self.assertEqual(manage.drift(self.baseline, current)["new"], ["research/new.md"])

    def test_campaign_runtime_and_worktree_git_metadata_are_excluded(self):
        self.cat["inventory_policy"]["pruned_directory_names"].append(".campaigns")
        self.cat["inventory_policy"]["excluded_paths"].append(".git")
        (self.root / ".campaigns/demo/worktree").mkdir(parents=True)
        (self.root / ".campaigns/demo/worktree/proof.md").write_text("runtime copy")
        (self.root / ".git").write_text("gitdir: fixture")
        current = manage.discover(self.root, self.cat)
        self.assertFalse(any(p.startswith(".campaigns/") or p == ".git"
                             for p in current["files"]))

    def test_campaign_frontier_stays_in_checkpoint_directory(self):
        (self.root / "PROJECT_MAP.md").write_text("primary entry stays untouched")
        self.cat["frontier_path"] = "notes/project-map/FRONTIER.md"
        self.assertEqual(self.cli("render").returncode, 0)
        self.assertEqual((self.root / "PROJECT_MAP.md").read_text(), "primary entry stays untouched")
        self.assertTrue((self.root / "notes/project-map/FRONTIER.md").is_file())
        self.assertEqual(self.cli("render", "--check").returncode, 0)

    def test_frontier_path_cannot_write_arbitrary_files(self):
        self.cat["frontier_path"] = "research/proof.md"
        with self.assertRaises(ValueError):
            manage.render(self.cat, self.baseline)

    def test_programme_navigation_and_missing_document(self):
        self.cat["programme"] = {"programme": "notes/project-map/PROGRAMME.md"}
        self.assertIn("missing programme document", self.errors())
        (self.root / "notes/project-map/PROGRAMME.md").write_text("# Programme\n")
        self.assertEqual(self.errors(), "")
        self.assertIn("PROGRAMME.md", manage.render(self.cat, self.baseline)["PROJECT_MAP.md"])

    def test_new_family_and_branch(self):
        (self.root / "new-family/mission-M02").mkdir(parents=True)
        (self.root / "new-family/proof.md").write_text("new")
        current = manage.discover(self.root, self.cat)
        self.assertEqual(current["files"]["new-family/proof.md"]["family"], "UNCLASSIFIED")
        self.assertIn("new-family/mission-M02", manage.drift(self.baseline, current)["new_branches"])

    def test_new_branch_in_existing_ledger(self):
        with (self.root / "research/ledger.md").open("a") as stream:
            stream.write("### L-0002 - Follow-up\n")
        delta = manage.drift(self.baseline, manage.discover(self.root, self.cat))
        self.assertEqual(len(delta["new_branches"]), 1)

    def test_branch_search_does_not_match_generic_family_links(self):
        self.cat["coverage"][0]["records"].append("HB-M340")
        branches = manage.branches_covered(self.baseline, self.cat)
        self.assertFalse(any(manage.branch_matches(b, "M340") for b in branches))
        self.assertEqual(sum(manage.branch_matches(b, "M01") for b in branches), 1)
        self.assertEqual(sum(manage.branch_matches(b, "L-0001") for b in branches), 1)

    def test_irrelevant_log_growth(self):
        (self.root / "research/run.log").write_text("many more runtime lines\n")
        self.assertFalse(any(manage.drift(self.baseline, manage.discover(self.root, self.cat)).values()))

    def test_invalidated_transitive_prerequisite(self):
        self.cat["records"][0]["effective_status"] = "rejected"
        errors = self.errors()
        self.assertIn("unsupported transitive prerequisite: B", errors)
        self.assertIn("unsupported transitive prerequisite: C", errors)

    def test_logical_cycle(self):
        self.cat["records"][0]["dependencies"] = ["C"]
        self.assertIn("logical cycle", self.errors())

    def test_historical_cycle_is_not_logical(self):
        self.cat["relations"] = [dict(type="historical-influence", **{"from": a, "to": b},
                                      reason="fixture", evidence=["proof"])
                                 for a, b in (("A", "C"), ("C", "A"))]
        self.assertEqual(self.errors(), "")

    def test_required_guard_and_alias(self):
        self.cat["records"][0]["guards"] = ""
        self.cat["records"][1]["aliases"] = ["A"]
        self.assertIn("missing guards: A", self.errors())
        self.assertIn("duplicate record ID or alias", self.errors())

    def test_missing_evidence_and_verdict(self):
        self.cat["records"][0]["evidence"] = ["unknown"]
        self.cat["records"][0]["adjudications"] = []
        self.assertIn("missing source: A: unknown", self.errors())
        self.assertIn("accepted without verdict: A", self.errors())

    def test_locator_and_reviewed_version(self):
        self.cat["sources"]["proof"]["checked_locators"] = ["not there"]
        self.cat["sources"]["proof"]["reviewed_sha256"] = "0" * 64
        self.assertIn("missing evidence locator", self.errors())
        self.assertIn("reviewed-version mismatch", self.errors())

    def test_broken_link_and_anchor(self):
        text = "[missing](no.md) [anchor](research/proof.md#absent)"
        self.assertEqual(len(manage.link_errors(self.root, "PROJECT_MAP.md", text)), 2)
        self.assertFalse(manage.link_errors(self.root, "PROJECT_MAP.md",
                                           "[ok](research/proof.md#frozen-theorem)"))

    def test_symlinks_are_not_followed(self):
        (self.root / "research/link").symlink_to(self.root / "research", target_is_directory=True)
        current = manage.discover(self.root, self.cat)
        self.assertEqual(current["files"]["research/link"]["mode"], "symlink-not-followed")
        self.assertFalse(any(p.startswith("research/link/") for p in current["files"]))

    def test_stale_view_and_branch_index(self):
        self.assertEqual(self.cli("render").returncode, 0)
        self.assertEqual(self.cli("render", "--check").returncode, 0)
        (self.root / "PROJECT_MAP.md").write_text("manual drift")
        self.assertNotEqual(self.cli("render", "--check").returncode, 0)
        self.cli("render")
        (self.root / "notes/project-map/branch-coverage.json").write_text("[]")
        checked = self.cli("validate")
        self.assertNotEqual(checked.returncode, 0)
        self.assertIn("stale/missing branch coverage", checked.stdout)

    def test_baseline_replacement_needs_receipt(self):
        output = str(self.root / "notes/project-map/inventory.json")
        denied = self.cli("inventory", "--output", output)
        self.assertNotEqual(denied.returncode, 0)
        allowed = self.cli("inventory", "--output", output, "--accept-reviewed",
                           "--review-receipt", "notes/project-map/UPDATE_PROTOCOL.md")
        self.assertEqual(allowed.returncode, 0, allowed.stderr)


class RetrievalChecks(unittest.TestCase):
    def test_sparse_candidate_is_not_promoted_by_consolidation(self):
        folder = Path(__file__).resolve().parent
        cat = manage.read_json(folder / "catalogue.json")
        records = {r["id"]: r for r in cat["records"]}
        candidate = records["P-SPARSE-EXACT"]
        self.assertEqual(candidate["effective_status"], "provisional")
        self.assertEqual(candidate["adjudications"], [])
        self.assertIn("implementation", candidate["open_obligations"])
        self.assertEqual(records["S-SPARSE"]["effective_status"], "accepted-inherited")

    def test_connected_genus_acceptance_leaves_global_question_open(self):
        folder = Path(__file__).resolve().parent
        cat = manage.read_json(folder / "catalogue.json")
        records = {r["id"]: r for r in cat["records"]}
        theorem = records["S-GENUS-FPT"]
        self.assertEqual(theorem["model"], "connected-endpoint")
        self.assertEqual(theorem["effective_status"], "accepted-inherited")
        self.assertIn("C^(g+1)", theorem["claim"])
        self.assertEqual(records["G-ALL"]["effective_status"], "open")

    def test_documentary_retrieval_contracts(self):
        folder = Path(__file__).resolve().parent
        cat = manage.read_json(folder / "catalogue.json")
        checks = manage.read_json(folder / "retrieval_checks.json")["checks"]
        records = {r["id"]: r for r in cat["records"]}
        for check in checks:
            with self.subTest(question=check["id"]):
                selected = [records[rid] for rid in check["records"]]
                for rid, status in check["expected_status"].items():
                    self.assertEqual(records[rid]["effective_status"], status)
                payload = json.dumps(selected)
                for required in check["required_text"]:
                    self.assertIn(required, payload)
                for sid in check["source_ids"]:
                    self.assertIn(sid, cat["sources"])
                self.assertTrue(check["answer"])
                self.assertTrue(check["initial_retrieval_issue"])


if __name__ == "__main__":
    unittest.main()
