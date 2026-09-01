# M335 run manifest

Date: 2026-08-14 UTC

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: 3.12.3.
- Random seeds: none; deterministic exact-rational guard.
- Nonstandard dependencies: none.
- Analytic object: fully combined M313/M319 profile-edge token law with
  corrected `c_X`, literal zero slots, both channels, all `T/S/N`, phases,
  seams, incidences, and representation weights retained.
- Sole computation: `k=9,n=27,H_2`; no other rank/row/surgery.
- Command:

```text
python3 -B slpfstar_k9_h2_guard.py \
  --repo /home/nico/projects/research_projects/reversible_circuits \
  --output slpfstar_k9_h2_results.json
```

The guard SHA-gates M323, M330, and the M297 primitive, enumerates the one
predeclared row in lexicographic order, and stops at the first failed frozen
clause. It stopped on token 1 at reverse-residual sign landing. It did not
test exceptional Borel bounds or any downstream statement.

