# M311 Dependency Audit

Date: 2026-08-14 UTC

The two accepted source locks were independently measured as

```text
M307  41d6096e07da79c374a06947a882820a3e470aa9fb6415217909cb4404bf765e
M308  37dbb530c567545cc25effa6902708a847c40daae3ff79487e46e0a4d91d1b4f
```

Every payload named in both inventories passes `sha256sum -c SHA256SUMS`.
M308 itself records and verifies the recursive M300/M303 and earlier source
locks.  Only these accepted inputs were used:

- exact positive `x_c,y_d` masses with equal total mass;
- exact QTI_1 and the complete-middle response convention;
- `R_c=A_c-B_c` and its crossing orientation;
- the finite `k=9` QCP obstruction and positive complete aggregates, only as
  prior finite facts.

No MCLP, GOCI, OCI, CP, MS, FCL1, gap, mixing, or Terminal conclusion was
imported.  No source artifact was modified.
