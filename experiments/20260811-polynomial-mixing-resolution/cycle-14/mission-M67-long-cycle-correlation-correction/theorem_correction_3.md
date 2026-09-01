# M67 theorem correction 3: one-edge cyclic-start count

Date: 2026-08-12. This append-only correction supersedes the sentence in
Theorem Section 1.1 beginning `There are n/2 unoriented edges for each value`.
For odd `n`, the correct counting statement is:

```text
For each d=1,...,n-1 there are n cyclic starts r for the oriented
description (r,r+d). The d and n-d terms describe the same n unoriented
edges, so every unoriented edge is counted twice in the full d-sum.
Consequently the total edge sum equals n/2 times the displayed d-sum.
```

Together with `|a((r,r+d))|^2=16sin^4(pi d/n)`, this gives the unchanged
coefficient `8n` in equation (1.4). The old wording was literally false; the
formula and every subsequent asymptotic were already correct.
