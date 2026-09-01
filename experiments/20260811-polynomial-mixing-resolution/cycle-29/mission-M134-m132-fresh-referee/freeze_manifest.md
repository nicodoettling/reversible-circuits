# M134 freeze manifest

Frozen: 2026-08-13 UTC.

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Frozen payload hashes

```text
1816fc82f4935da762fc343298f2e189a78557e2aa6be37f7e8d63ac8bb7cec5  plan.md
d540f289b9788de459afc07dbcb52fc8aba9c76cf8a178c4f0983acb51179b24  checkpoint.md
f8885db6b8485d230d3f46bd261504bad5950a141d757813db87f82e5a123c9b  independent_referee.py
97e898b9b1a55d4b86ed47664272455e94f3d819e02116d4c0eb2cea37825d09  independent_results.json
40018b30cefc5ea69068984a30ce3be4c0e14f3f64d2b96a16f67d30ac021c20  report.md
```

## Reproduction

```text
python3 -B independent_referee.py
python3 -c 'from pathlib import Path; compile(Path("independent_referee.py").read_text(), "independent_referee.py", "exec"); print("compile ok")'
python3 -c 'import json; p=json.load(open("independent_results.json")); assert p["verdict"]=="ACCEPT"; print("assertions ok")'
```

Python `3.12.3`, dependencies `{}`, seed `null`; the computation is
deterministic. The exact run takes about eight seconds in the recorded
environment.

## Frozen verdict and scope

```text
ACCEPT M132 AT ITS STATED NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

Accepted: the exact `d=4` collision for the defined `O(d^40)` descriptor,
the subgroup orders and hand descriptions, the conflict graph as a necessary
coloring obstruction, the complete `d=3` figures, and conditional recovery
with the exact factor-`d` root quotient.

Unresolved: a general adjacent-value polynomial schedule cover, simultaneous
braid realization, UST basis-exchange routing, full rooted-product comparison,
every physical/original gap claim, and both terminal outcomes.
