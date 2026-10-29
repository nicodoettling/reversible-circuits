#!/usr/bin/env python3
"""Documentary research catalogue checks; never proof certification."""

import argparse
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote


MAP_DIR = Path("notes/project-map")
VIEWS = {
    "PROJECT_MAP.md": "frontier",
    "notes/project-map/RESULTS.md": "results",
    "notes/project-map/OBSTRUCTIONS.md": "obstructions",
    "notes/project-map/TARGETS.md": "targets",
    "notes/project-map/COVERAGE.md": "coverage",
}
STATUSES = {"accepted-inherited", "accepted-reviewed", "conditional",
            "provisional", "open", "rejected", "superseded", "unresolved"}
DEPTHS = {"inventory-only", "summary-only", "statement-traced",
          "statement-and-verdict-traced", "proof-reviewed",
          "experiment-reproduced", "formalization-checked"}
RELATIONS = {"supersedes", "refutes", "specializes", "covers", "analogous-to",
             "historical-influence", "does-not-imply"}


def view_paths(catalogue):
    frontier = catalogue.get("frontier_path", "PROJECT_MAP.md")
    if frontier not in {"PROJECT_MAP.md", "notes/project-map/FRONTIER.md"}:
        raise ValueError("frontier_path must be the project or campaign-local map entry point")
    return {frontier if path == "PROJECT_MAP.md" else path: kind
            for path, kind in VIEWS.items()}


def read_json(path):
    return json.loads(path.read_text())


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe_path(root, relative):
    path = root / relative
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"external evidence path: {relative}")
    return path


def family_for(path, catalogue):
    matches = [(len(p), f["id"]) for f in catalogue["coverage"]
               for p in f["prefixes"] if path == p or path.startswith(p.rstrip("/") + "/")]
    return max(matches)[1] if matches else "UNCLASSIFIED"


def discover(root, catalogue):
    policy = catalogue["inventory_policy"]
    files, branches = {}, {}
    for directory, dirs, names in os.walk(root, followlinks=False):
        rel_dir = Path(directory).relative_to(root).as_posix()
        dirs[:] = sorted(d for d in dirs if d not in policy["pruned_directory_names"]
                         and not any((Path(rel_dir) / d).as_posix() == p
                                     for p in policy["excluded_paths"]))
        for d in list(dirs):
            path = Path(directory) / d
            if path.is_symlink():
                names.append(d)
                dirs.remove(d)
            elif d.startswith("mission-"):
                rel = path.relative_to(root).as_posix()
                branches[rel] = {"path": rel, "kind": "mission-directory",
                                 "family": family_for(rel, catalogue)}
        for name in sorted(names):
            path = Path(directory) / name
            rel = path.relative_to(root).as_posix()
            if rel in policy["excluded_paths"]:
                continue
            if any(fnmatch.fnmatch(name, p) for p in policy["excluded_filename_patterns"]):
                continue
            family = family_for(rel, catalogue)
            if path.is_symlink():
                files[rel] = {"family": family, "mode": "symlink-not-followed",
                              "target": os.readlink(path)}
                continue
            if not path.is_file():
                files[rel] = {"family": family, "mode": "special-not-read"}
                continue
            telemetry = any(fnmatch.fnmatch(name, p) for p in policy["telemetry_patterns"])
            item = {"family": family, "mode": "telemetry" if telemetry else "research"}
            if not telemetry:
                item["sha256"] = digest(path)
            else:
                item["bytes_at_discovery"] = path.stat().st_size
            files[rel] = item
            if rel in policy["branch_heading_sources"]:
                for line in path.read_text().splitlines():
                    if re.match(r"^#{2,3} (?:L-|CP-)\d+", line):
                        heading = line.lstrip("# ")
                        key = rel + "#" + slug(heading)
                        branches[key] = {"path": rel, "heading": heading,
                                         "kind": "ledger-entry", "family": family}
    return {"schema_version": 1, "files": files, "branches": branches}


def slug(text):
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def branches_covered(snapshot, catalogue):
    result = []
    rules = catalogue.get("branch_overrides", [])
    families = {f["id"]: f for f in catalogue["coverage"]}
    for key, branch in snapshot["branches"].items():
        matching = [r for r in rules if key.startswith(r["prefix"])]
        rule = max(matching, key=lambda r: len(r["prefix"])) if matching else None
        family = families.get(branch["family"], {})
        result.append({"id": key, **branch,
                       "disposition": rule["disposition"] if rule else family.get("branch_disposition", "pending"),
                       "records": rule["records"] if rule else [],
                       "depth": rule["depth"] if rule else "inventory-only"})
    return result


def branch_matches(item, query):
    fields = (item["id"], item["path"], item.get("heading", ""), *item["records"])
    return query.lower() in " ".join(fields).lower()


def descendants(records, initial):
    affected = set(initial)
    while True:
        more = {r["id"] for r in records if set(r["dependencies"]) & affected}
        if more <= affected:
            return sorted(affected)
        affected |= more


def drift(baseline, current):
    old = {p: v for p, v in baseline["files"].items() if v["mode"] != "telemetry"}
    new = {p: v for p, v in current["files"].items() if v["mode"] != "telemetry"}
    return {"new": sorted(new.keys() - old.keys()),
            "missing": sorted(old.keys() - new.keys()),
            "changed": sorted(p for p in old.keys() & new.keys() if old[p] != new[p]),
            "new_branches": sorted(current["branches"].keys() - baseline["branches"].keys()),
            "missing_branches": sorted(baseline["branches"].keys() - current["branches"].keys())}


def link_errors(root, relative, text):
    errors = []
    for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
        if re.match(r"(?:https?://|mailto:)", target):
            continue
        path_part, _, anchor = unquote(target).partition("#")
        path = root / relative if not path_part else (root / relative).parent / path_part
        if not path.resolve().is_relative_to(root.resolve()):
            errors.append(f"external local link: {relative}: {target}")
        elif not path.exists():
            errors.append(f"missing local link: {relative}: {target}")
        elif anchor and path.suffix == ".md":
            content = path.read_text()
            anchors = {slug(line.lstrip("# ")) for line in content.splitlines() if line.startswith("#")}
            anchors |= set(re.findall(r'<a id="([^"]+)"', content))
            if anchor not in anchors:
                errors.append(f"missing anchor: {relative}: {target}")
    return errors


def validate(root, cat):
    errors = []
    records = cat["records"]
    ids = [r["id"] for r in records]
    aliases = [a for r in records for a in r.get("aliases", [])]
    if len(set(ids + aliases)) != len(ids + aliases):
        errors.append("duplicate record ID or alias")
    by_id = {r["id"]: r for r in records}
    families = {f["id"] for f in cat["coverage"]}
    sources = cat["sources"]
    changed_sources = set()
    for sid, source in sources.items():
        try:
            path = safe_path(root, source["path"])
            if not path.is_file() or digest(path) != source["sha256"]:
                errors.append(f"evidence drift: {sid}: {source['path']}")
                changed_sources.add(sid)
            if source.get("reviewed_sha256") and source["sha256"] != source["reviewed_sha256"]:
                errors.append(f"reviewed-version mismatch: {sid}")
            if path.is_file() and path.suffix in {".md", ".tex", ".py"}:
                content = path.read_text()
                for locator in source.get("checked_locators", []):
                    if locator not in content:
                        errors.append(f"missing evidence locator: {sid}: {locator}")
        except (ValueError, OSError) as exc:
            errors.append(str(exc))
        if not source.get("read_scope"):
            errors.append(f"missing read scope: {sid}")
        if not source.get("checked_locators"):
            errors.append(f"missing exact evidence locator: {sid}")
    for record in records:
        rid = record["id"]
        for field in ("version", "title", "kind", "claim", "model", "parameters", "guards",
                      "source_claimed_status", "effective_status", "check_depth", "evidence",
                      "limitations", "assumptions", "open_obligations", "review_binding"):
            if not record.get(field):
                errors.append(f"missing {field}: {rid}")
        if record["effective_status"] not in STATUSES or record["check_depth"] not in DEPTHS:
            errors.append(f"invalid status/depth: {rid}")
        if record["family"] not in families or record["model"] not in cat["models"]:
            errors.append(f"unknown family/model: {rid}")
        for sid in record["evidence"] + record.get("adjudications", []):
            if sid not in sources:
                errors.append(f"missing source: {rid}: {sid}")
        if record["effective_status"].startswith("accepted") and not record.get("adjudications"):
            errors.append(f"accepted without verdict: {rid}")
        for dep in record["dependencies"]:
            if dep not in by_id:
                errors.append(f"unknown dependency: {rid}: {dep}")
    visiting, visited = set(), set()

    def visit(rid):
        if rid in visiting:
            errors.append(f"logical cycle at {rid}")
            return
        if rid in visited or rid not in by_id:
            return
        visiting.add(rid)
        for dep in by_id[rid]["dependencies"]:
            visit(dep)
        visiting.remove(rid)
        visited.add(rid)

    for rid in ids:
        visit(rid)
    unsupported = {r["id"] for r in records if not r["effective_status"].startswith("accepted")}
    inherited_bad = set(descendants(records, unsupported)) - unsupported
    for rid in sorted(inherited_bad):
        if by_id[rid]["effective_status"].startswith("accepted"):
            errors.append(f"accepted with unsupported transitive prerequisite: {rid}")
    direct_drift = {r["id"] for r in records if changed_sources & set(r["evidence"] + r.get("adjudications", []))}
    if direct_drift:
        errors.append("affected claims (recheck, not automatic refutation): " + ", ".join(descendants(records, direct_drift)))
    for relation in cat["relations"]:
        if relation["type"] not in RELATIONS or any(relation[k] not in by_id for k in ("from", "to")):
            errors.append(f"invalid typed relation: {relation}")
        if not relation.get("reason") or not relation.get("evidence") or any(s not in sources for s in relation["evidence"]):
            errors.append(f"relation without evidence: {relation}")
    for family in cat["coverage"]:
        if not family.get("disposition") or not family.get("read_depth"):
            errors.append(f"missing coverage disposition: {family['id']}")
        for rid in family["records"]:
            if rid not in by_id:
                errors.append(f"missing coverage record: {rid}")
    target_ids = [t["id"] for t in cat["targets"]]
    if len(set(target_ids)) != len(target_ids):
        errors.append("duplicate target IDs")
    for target in cat["targets"]:
        for field in ("obligation", "nearest", "advance", "first_test", "positive", "negative",
                      "stop_or_pivot", "effort", "uncertainty", "rationale"):
            if not target.get(field):
                errors.append(f"missing target {field}: {target['id']}")
        for rid in target["nearest"]:
            if rid not in by_id:
                errors.append(f"unknown target predecessor: {rid}")
    for rule in cat.get("branch_overrides", []):
        if any(rid not in by_id for rid in rule["records"]):
            errors.append(f"unknown branch record: {rule['prefix']}")
    for external in cat.get("external_inputs", []):
        for field in ("id", "citation", "url", "locator", "transfer", "review_scope"):
            if not external.get(field):
                errors.append(f"missing external input {field}: {external.get('id')}")
    for brief in cat.get("briefs", []):
        if not (root / brief["path"]).is_file() or not brief.get("disposition"):
            errors.append(f"missing brief/disposition: {brief}")
    for name in catalogue_programme_paths(cat):
        path = safe_path(root, name)
        if not path.is_file():
            errors.append(f"missing programme document: {name}")
        else:
            errors.extend(link_errors(root, name, path.read_text()))
    for name in view_paths(cat):
        if (root / name).exists():
            errors.extend(link_errors(root, name, (root / name).read_text()))
    return errors


def relative_link(view, path):
    return os.path.relpath(path, Path(view).parent).replace(os.sep, "/")


def catalogue_programme_paths(cat):
    return list(cat.get("programme", {}).values())


def render(cat, snapshot):
    outputs = {}
    records = cat["records"]
    generated = "<!-- Generated by notes/project-map/manage.py render; edit catalogue.json. -->\n"
    for path, kind in view_paths(cat).items():
        def source_link(sid):
            source = cat["sources"][sid]
            return f"[{sid}]({relative_link(path, source['path'])})"

        def record_link(rid):
            rec = next(r for r in records if r["id"] == rid)
            dest = "notes/project-map/OBSTRUCTIONS.md" if rec["view"] == "obstructions" else "notes/project-map/RESULTS.md"
            return f"[{rid}]({relative_link(path, dest)}#{rid.lower()})"

        lines = [generated]
        if kind == "frontier":
            lines += ["# Research Project Map", "", f"Documentary consolidation: {cat['date']} ({cat['timezone']}).", ""]
            for paragraph in cat["project"]["frontier_paragraphs"]:
                lines += [paragraph, ""]
            for heading, items in cat["project"]["routes"].items():
                lines += [f"## {heading}", ""]
                for item in items:
                    lines += [f"- {item['text']} {record_link(item['record'])}"]
                lines += [""]
            lines += ["## Read Next", ""]
            for name in ("RESULTS", "OBSTRUCTIONS", "TARGETS", "COVERAGE", "UPDATE_PROTOCOL"):
                lines += [f"- [{name}]({relative_link(path, 'notes/project-map/' + name + '.md')})"]
            for label, programme_path in cat.get("programme", {}).items():
                lines += [f"- [{label.replace('_', ' ').title()}]({relative_link(path, programme_path)})"]
            lines += ["", "## Maintenance", "", "```sh", *cat["maintenance_commands"], "```", "",
                      "The catalogue is documentary evidence, not a new mathematical acceptance. "
                      "Changed evidence or new discoveries make checks fail without silently changing claims."]
        elif kind in {"results", "obstructions"}:
            lines += ["# " + ("Surviving Results and Open Obligations" if kind == "results" else "Obstructions and Failed Approaches"), "",
                      "Statuses below are scoped to exact claims. `accepted-inherited` means a recorded "
                      "internal verdict was traced, not that this mapping independently proved it.", ""]
            if kind == "results":
                lines += ["## Models and Policies", ""]
                for model, description in cat["models"].items():
                    lines += [f"- **{model}:** {description}"]
                lines += [""]
                for paragraph in cat.get("policy_definitions", []):
                    lines += [paragraph, ""]
            for r in records:
                if r["view"] != kind:
                    continue
                lines += [f'<a id="{r["id"].lower()}"></a>', f"## {r['id']}: {r['title']}", "",
                          r["claim"], "", f"- Effective status: **{r['effective_status']}**; source: {r['source_claimed_status']}",
                          f"- Mapping depth: {r['check_depth']}. {r['checked']}",
                          f"- Model: {r['model']}; parameters: {r['parameters']}",
                          f"- Guards: {r['guards']}", f"- Assumptions: {r['assumptions']}",
                          f"- Remaining obligation: {r['open_obligations']}",
                          f"- Limitations: {r['limitations']}",
                          f"- Version / verdict binding: {r['review_binding']}",
                          "- Evidence: " + ", ".join(source_link(s) for s in r["evidence"]),
                          "- Adjudication: " + (", ".join(source_link(s) for s in r.get("adjudications", [])) or "None recorded for this scope."),
                          "- Logical dependencies: " + (", ".join(record_link(d) for d in r["dependencies"]) or "None at this map's granularity."),
                          f"- Regressions / disagreements: {r['regressions']} {r['disagreements']}", ""]
            if kind == "results":
                lines += ["## Imported Literature", "", "These are inherited source translations, not a fresh literature audit.", ""]
                for ext in cat.get("external_inputs", []):
                    lines += [f"- **{ext['id']}**: [{ext['citation']}]({ext['url']}), {ext['locator']}. "
                              f"{ext['transfer']} {ext['review_scope']}"]
                lines += ["", "## Nonlogical Relations", "", "These links do not supply proof prerequisites.", ""]
                for rel in cat["relations"]:
                    lines += [f"- {record_link(rel['from'])} **{rel['type']}** {record_link(rel['to'])}: "
                              f"{rel['reason']} " + ", ".join(source_link(s) for s in rel['evidence'])]
        elif kind == "targets":
            lines += ["# Next Investigations", "", "Recommendations, not launched runs. Effort estimates are planning judgments, not promises.", ""]
            for t in sorted(cat["targets"], key=lambda t: t["rank"]):
                lines += [f"## {t['id']}: {t['title']} ({t['tier']})", "", t["obligation"], "",
                          "- Nearest evidence: " + ", ".join(record_link(r) for r in t["nearest"])]
                for field in ("advance", "first_test", "positive", "negative", "stop_or_pivot", "effort", "uncertainty", "rationale"):
                    lines += [f"- {field.replace('_', ' ').capitalize()}: {t[field]}"]
                lines += [""]
            lines += ["## Historical Launch Briefs", "", "Original briefs are preserved; these dispositions govern map-based reuse.", ""]
            for brief in cat["briefs"]:
                lines += [f"- [{brief['path']}]({relative_link(path, brief['path'])}): {brief['disposition']}"]
        else:
            lines += ["# Coverage and Conflicts", "", cat["coverage_scope"], "",
                      f"Discovery baseline: {len(snapshot['files'])} entries; {len(snapshot['branches'])} ledger/mission branches. "
                      "Counts are navigation inventory, not numbers of reviewed theorems.", ""]
            for family in cat["coverage"]:
                count = sum(f["family"] == family["id"] for f in snapshot["files"].values())
                lines += [f"## {family['id']}: {family['title']}", "",
                          f"{count} discovered entries. {family['disposition']}. Depth: {family['read_depth']}.", "",
                          family["limits"], "",
                          "Records: " + (", ".join(record_link(r) for r in family["records"]) or "Pending; no mathematical record inferred."), ""]
            lines += ["## Unresolved and Reconciled Discrepancies", ""]
            for conflict in cat["conflicts"]:
                lines += [f"- **{conflict['id']} ({conflict['status']}):** {conflict['description']} " +
                          ", ".join(source_link(s) for s in conflict["sources"])]
            lines += ["", "## Read Register", "", "Full files are fingerprinted; listed read scopes may be excerpts only.", ""]
            for sid, source in cat["sources"].items():
                lines += [f"- {source_link(sid)}: {source['read_scope']}"]
            lines += ["", "## Branch Retrieval", "", "```sh",
                      "python3 -B notes/project-map/manage.py branches --query M340",
                      "python3 -B notes/project-map/manage.py branches --query L-0336", "```", "",
                      "Unselected mission directories and ledger entries remain inventory-only/pending. "
                      "A family grouping is not blanket acceptance. Full branch dispositions are in branch-coverage.json."]
        outputs[path] = "\n".join(lines).rstrip() + "\n"
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("check-freshness")
    rnd = sub.add_parser("render")
    rnd.add_argument("--check", action="store_true")
    inv = sub.add_parser("inventory")
    inv.add_argument("--output", type=Path, required=True)
    inv.add_argument("--review-receipt", help="Required to write/replace the reviewed baseline.")
    inv.add_argument("--accept-reviewed", action="store_true")
    for name in ("find", "branches"):
        sub.add_parser(name).add_argument("--query", default="")
    args = parser.parse_args()
    root = args.root.resolve()
    cat = read_json(root / MAP_DIR / "catalogue.json")
    baseline_path = root / MAP_DIR / "inventory.json"
    if args.command == "inventory":
        output = args.output.resolve()
        if output == baseline_path.resolve():
            if not args.accept_reviewed or not args.review_receipt or not (root / args.review_receipt).is_file():
                parser.error("baseline replacement requires --accept-reviewed and an existing --review-receipt")
        snapshot = discover(root, cat)
        snapshot["review_receipt"] = args.review_receipt
        output.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n")
        print(f"Inventory: {len(snapshot['files'])} entries, {len(snapshot['branches'])} branches -> {output}")
        return
    if args.command == "find":
        for rec in cat["records"]:
            if args.query.lower() in json.dumps(rec).lower():
                print(json.dumps({**rec, "resolved_evidence": {s: cat["sources"][s] for s in rec["evidence"]}}, indent=2))
        return
    baseline = read_json(baseline_path)
    if args.command == "branches":
        for item in branches_covered(baseline, cat):
            if branch_matches(item, args.query):
                print(json.dumps(item, ensure_ascii=True))
        return
    if args.command == "check-freshness":
        differences = drift(baseline, discover(root, cat))
        print(json.dumps(differences, indent=2))
        sys.exit(1 if any(differences.values()) else 0)
    if args.command == "validate":
        errors = validate(root, cat)
        unknown = [p for p, f in baseline["files"].items()
                   if f["family"] == "UNCLASSIFIED" and f["mode"] == "research"]
        errors += [f"unclassified discovered source: {p}" for p in unknown]
        expected_branches = branches_covered(baseline, cat)
        branch_file = root / MAP_DIR / "branch-coverage.json"
        if not branch_file.exists() or read_json(branch_file) != expected_branches:
            errors.append("stale/missing branch coverage: run render")
        print("\n".join(errors) if errors else f"PASS: {len(cat['records'])} records, {len(cat['sources'])} pinned sources; no mathematical verification implied.")
        sys.exit(bool(errors))
    outputs = render(cat, baseline)
    stale = []
    for relative, content in outputs.items():
        path = root / relative
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(relative)
        else:
            path.write_text(content)
    branch_content = json.dumps(branches_covered(baseline, cat), indent=2, sort_keys=True) + "\n"
    branch_path = root / MAP_DIR / "branch-coverage.json"
    if args.check:
        if not branch_path.exists() or branch_path.read_text() != branch_content:
            stale.append(str(MAP_DIR / "branch-coverage.json"))
    else:
        branch_path.write_text(branch_content)
    print("Stale: " + ", ".join(stale) if stale else "PASS: deterministic views" if args.check else "Rendered map views and branch coverage")
    sys.exit(bool(stale))


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.stdout.close()
        sys.exit(0)
