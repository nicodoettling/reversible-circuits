"""Check the distinct decoded-tree macro kernel and its full Hurwitz lifts."""
from pathlib import Path
from itertools import product
import hashlib
import importlib.util
import json
import platform
import subprocess

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


core = load('lift_core', HERE / 'check.py')
codec_path = HERE.parent / '20261013-single-cycle-walk/check.py'
slides_path = HERE.parent / '20261014-tree-slides/check.py'
codec = load('cycle_codec', codec_path)
slides = load('tree_slides', slides_path)


def reduced_path(word, n):
    w, ops = word, []
    end = len(w)
    for v in range(n-1, 0, -1):
        i = next((i for i in range(end) if v in w[i]), None)
        if i is None:
            continue
        while i < end-1:
            assert w[i] != w[i+1]
            sign = 1 if v not in w[i+1] else -1
            w = core.hurwitz(w, i, sign)
            ops.append((i, sign))
            i += 1
        end -= 1
    assert w == core.canonical(core.evaluate(word, n))
    assert len(ops) <= n*(n-1)
    return ops


def check_n(n):
    trees = [codec.code_to_tree(n, code) for code in product(range(n), repeat=n-2)]
    words = {t: codec.tree_to_word(n, t) for t in trees}
    routes = {t: reduced_path(w, n) for t, w in words.items()}
    assert len(set(words.values())) == len(trees)
    neighbors = {t: slides.slides(n, t) for t in trees}
    transitions = max_length = 0
    for t, w in words.items():
        assert codec.word_to_tree(n, w) == t
        assert core.evaluate(w, n) == codec.target(n)
        for u in neighbors[t]:
            assert t in neighbors[u]
            ops = routes[t] + [(i, -sign) for i, sign in reversed(routes[u])]
            assert len(ops) <= 2*n*(n-1)
            z = w
            for i, sign in ops:
                z = core.hurwitz(z, i, sign)
                assert core.evaluate(z, n) == codec.target(n)
            assert z == words[u]
            transitions += 1
            max_length = max(max_length, len(ops))
    return dict(N=n, trees=len(trees), directed_slide_transitions=transitions,
                max_primitive_lift_length=max_length, path_bound=2*n*(n-1),
                codec_and_every_primitive_endpoint_ok=True,
                reverse_slide_and_uniform_macro_symmetry_ok=True)


def main():
    result = dict(python=platform.python_version(), dependencies='standard library only',
                  commit=subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
                  command='python3 -B ' + str(HERE.relative_to(Path.cwd()) / 'tree_check.py'),
                  seeds='none: exhaustive deterministic enumeration',
                  imported_sources={str(p.relative_to(Path.cwd())):
                      hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in (HERE / 'check.py', codec_path, slides_path)})
    result['cases'] = [check_n(n) for n in range(2, 7)]
    result['status'] = 'all exact decoded-tree macro checks passed'
    (HERE / 'tree_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['cases'], indent=2))
    print(result['status'])


if __name__ == '__main__':
    main()
