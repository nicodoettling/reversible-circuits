#!/usr/bin/env python3
"""Read-only delivery consistency audit; writes only its own result JSON."""
import ast
import datetime
import hashlib
import json
from pathlib import Path
import platform
import subprocess

OWN = Path(__file__).resolve().parent
ROOT = OWN.parent.parent
REPO = ROOT.parent.parent
SNAP = OWN / 'synthesis-review-input'


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def semantic(value):
    """Ignore provenance/timing only; preserve every mathematical result."""
    omit = {'seconds', 'elapsed_seconds', 'actual_stack_forward_law_seconds',
            'forced_moments_seconds', 'top_integration_seconds', 'command',
            'git_status'}
    if isinstance(value, dict):
        return {k: semantic(v) for k, v in value.items() if k not in omit}
    if isinstance(value, list):
        return [semantic(v) for v in value]
    return value


def module_algorithm(path):
    tree = ast.parse(path.read_text())
    assert isinstance(tree.body[0], ast.Expr)
    assert isinstance(tree.body[0].value, ast.Constant)
    assert isinstance(tree.body[0].value.value, str)
    tree.body.pop(0)
    return ast.dump(tree, include_attributes=False)


def main():
    checks = {}
    frozen = {}
    for name in ['freeze_manifest.json', 'recursive_review_manifest.json']:
        for relative, expected in read(OWN / name)['payload_sha256'].items():
            assert sha(OWN / relative) == expected, relative
            frozen[str((OWN / relative).relative_to(REPO))] = expected
    prior = read(OWN / 'recursive_review_manifest.json')['reviewed_sha256']
    for relative, expected in prior.items():
        if relative not in ['proof.md', 'global_consequence.md', 'sample.py']:
            assert sha(ROOT / relative) == expected, relative
            frozen[str((ROOT / relative).relative_to(REPO))] = expected
    assert sha(ROOT / 'roles/r3-referee/blind_report.md') == 'e638cecd1c337a8d740be59f09aa7d9b895778616419dbcf85b3c9befde2250c'
    checks['frozen_hashes_verified'] = frozen
    for name in ['candidate_audit.md', 'global_audit.md']:
        p = ROOT / 'roles/r3-referee' / name
        checks['r3_' + name + '_sha256'] = sha(p)
    checks['r1_structural_audit_sha256'] = sha(ROOT / 'roles/r1-recursive/structural_audit.md')

    first = '## Frozen objects and theorem'
    last = '## Dependencies, first gap, and exclusions'
    old = (ROOT / 'roles/r1-recursive/proof.md').read_text()
    new = (SNAP / 'proof.md').read_text()
    assert old.split(first)[1].split(last)[0] == new.split(first)[1].split(last)[0]
    checks['canonical_mathematical_body_byte_equal'] = True
    assert module_algorithm(SNAP / 'sample.py') == module_algorithm(ROOT / 'roles/r3-referee/global-review-input/sample.py')
    checks['sample_ast_equal_except_module_docstring'] = True

    reruns = []
    for original, rerun in [
        ('roles/r1-recursive/results.json', 'coordinator_r1_results.json'),
        ('roles/r2-structural/recursive_independent_results.json', 'coordinator_recursive_forward_results.json'),
        ('roles/r1-recursive/structural_parser_results.json', 'coordinator_structural_parser_results.json')]:
        assert semantic(read(ROOT / original)) == semantic(read(ROOT / rerun)), (original, rerun)
        reruns.append({'original': original, 'rerun': rerun, 'all_semantic_results_equal': True})
    checks['coordinator_reruns'] = reruns
    parser = read(ROOT / 'coordinator_structural_parser_results.json')
    codes = [r['numeric_codes'] for r in parser['numeric']]
    assert codes == [1, 4, 15, 58]
    assert sum(r['partial_coefficients_checked'] for r in parser['numeric']) == 4431
    assert parser['labeled_macros'][-1]['macros'] == 1420
    checks['parser_codes_N2_to_N5'] = codes
    checks['parser_code_total'] = sum(codes)
    own = read(OWN / 'recursive_independent_results.json')
    assert sum(r['exact_moment_entries'] for r in own['forced_moments']) == 97232
    assert sum(r['word_count'] for r in own['actual_stack_forward_law']) == 5068
    r3 = read(ROOT / 'roles/r3-referee/candidate-check-results.json')
    assert [r3['moments'][k] for k in ['exact_full_moment_tables', 'forced_mass_queries_vs_blind_oracle', 'count_formula_queries']] == [7754, 11631, 3192]
    assert r3['actual_stack_replays']['actual_sampler_replays'] == 1488
    assert r3['deep_stack']['output_length'] == 1200 and 'stubbed' in r3['deep_stack']['scope']
    mass = read(ROOT / 'global_mass_results.json')
    assert len(mass['rows']) == 369 and mass['checks']['independent_count_cells'] == 91
    oldmass = read(ROOT / 'roles/r3-referee/global-review-input/global_mass_results.json')
    assert mass['rows'] == oldmass['rows']
    integration = read(ROOT / 'integration_results.json')
    assert integration['connected_valid_draws'] == 15 and integration['restricted_valid_draws'] == 51
    assert len(integration['invalid_inputs_rejected']) == 7
    checks['all_reported_targeted_test_counts_verified'] = True
    checks['global_certificate_rows_equal_reviewed_snapshot'] = 369

    initial = read(OWN / 'synthesis_input_manifest.json')
    assert not initial['manifest_inventory_symmetric_difference']
    assert not initial['preexisting_unlisted_research_files']
    allowed_stale = {str((ROOT / p).relative_to(REPO)) for p in ['coordinator_report.md', 'regression_registry.md', 'run_manifest.md']}
    assert set(initial['manifest_mismatches']) == allowed_stale
    checks['initial_inventory_complete'] = True
    checks['old_manifest_hashes_stale_only_for_review_corrections'] = sorted(allowed_stale)
    # Snapshot is exact input preservation; coordinator-owned root may later
    # change final status and inventory without changing these reviewed bytes.
    for row in initial['inputs']:
        assert sha(REPO / row['snapshot']) == row['sha256']
    checks['all_12_review_snapshots_hash_verified'] = True
    parsed = []
    for row in read(SNAP / 'artifact_manifest.json')['artifacts']:
        path = REPO / row['path']
        if path.suffix == '.py':
            compile(path.read_text(), str(path), 'exec')
            parsed.append(row['path'])
        elif path.suffix == '.json':
            read(path)
            parsed.append(row['path'])
    checks['existing_python_and_json_syntax_valid'] = parsed
    assert not list(ROOT.rglob('__pycache__'))
    assert not subprocess.check_output(['git', 'diff', '--name-only'], cwd=REPO, text=True).strip()
    checks['no_bytecode_cache_or_tracked_git_diff'] = True
    status = subprocess.check_output(['git', 'status', '--short'], cwd=REPO, text=True)
    result = {'version': 'R2-SYNTHESIS-v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'python': platform.python_version(), 'dependencies': 'standard library only',
              'command': 'timeout 30s python3 -B experiments/20260907-genus-one-sampler/roles/r2-structural/synthesis_checks.py',
              'random_seed': None, 'method': 'deterministic snapshot, syntax and exact saved-result comparison; no new sampler experiment',
              'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip(),
              'git_status': status, 'checks': checks, 'all_passed': True}
    (OWN / 'synthesis_checks.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'all_passed': True, 'frozen_payload_files_verified': len(frozen),
                      'syntax_files_checked': len(parsed), 'root_inventory_needs_planned_regeneration': True}))


if __name__ == '__main__':
    main()
