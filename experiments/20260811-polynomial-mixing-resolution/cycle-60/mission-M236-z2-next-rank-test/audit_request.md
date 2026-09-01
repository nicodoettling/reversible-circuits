# M236 fresh-audit request

Please perform a fresh immutable, no-import audit of frozen M236.

## Required checks

1. Run `sha256sum -c SHA256SUMS` in M236 and do not edit it.
2. Confirm `immutable_gate.md` predates the checker result and transcribes
   exactly the M231/M234 definitions of `late`, `ascent`, `epsilon`, `Z2`,
   and `Q B_d Q^-1`, with only `d=7` substituted.
3. Independently reconstruct the complete 1,296-tree root-leaf universe and
   all primary edits `{1,3,5,7,9}`. Do not import or read M236 code/results at
   runtime and do not enumerate a quotient graph or search for routes.
4. Verify descriptor/word assignment occurs before endpoint construction,
   both endpoints evaluate to identity, and chronological signed-Hurwitz
   replay passes exactly 6,480/6,480 primary rows.
5. Reconcile the six fixed non-Z2 families separately and verify the claimed
   7,776/7,776 secondary and 14,256/14,256 full-table counts.
6. Reproduce the per-edit Z2 class counts `9,6,4,3,2`, global count/word count
   20, closed/open counts `2,974/3,506`, maximum route length 21, the route
   histograms, and all normalized digests.
7. Audit the exact literal-word-kernel proof and the strict finite scope.

Classify every objection as material or nonmaterial. A source-order concern,
formula mismatch, incomplete universe, nonexact replay, hidden endpoint
lookup, digest mismatch, or overclaim is material. Do not infer an all-rank
route, every-color result, polynomial length, gap, mixing theorem, or Terminal
from a clean acceptance.

