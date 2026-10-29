# Bridge Projections and Replacement Endpoints

Objective: answer the user's projection/replacement questions for fixed,
nonadaptive positions in ordered transposition identity words. No background
run or extension of the completed genus-scaling run is authorized here.

Primary target is GLOBAL fixed-length uniform Omega(N,L), not conditional
connected-support uniformity. Also check which algebraic implications survive
connected conditioning. Products act rightmost first, labels are1..N.

Claims to falsify:

1. Every ordered k-subsequence has the same law as the first k gates, via a
   product-preserving Hurwitz stable sort that leaves selected gates unchanged.
2. For a selected tuple a, its number of global completions is
   Z_(L-k)((a1...ak)^-1). This determines the exact projection TV error.
3. Prefix-conjugating each gate is a bijection of both global and connected
   identity-word spaces. Replacing k gates independently by uniform
   transpositions yields endpoint law mu^k * rho, where rho is the product
   law of the original selected tuple under either uniform target.
4. Endpoint TV error against mu^(2k) is bounded by tuple TV error against
   independent uniform gates. One replacement is exactly mu^2.
5. Every projected product has transposition distance at most L-k.

Exact checks: N2,L2/4; N3,L2/4/6; N4,L4/6. Inspect all fixed index sets of
size at most2, all bridge words and all replacement choices. N4,L6 uses only
46656 candidate words; no large-N enumeration. Use integer counts/Fractions,
no stochastic conclusion or seed. Expected runtime below60s and512MiB. Execute
with an explicit60-second timeout and512MiB address limit. Retain complete
results.json and concise report.md, including failures.

Failure risks: noncommutative factor order, confusing raw selected gates with
conjugated defects, false exchangeability, dropping parity, connected/global
conditioning mismatch, or treating the 2k effective factors as independent.
Literature mixing corollaries are analytical dependencies, not verified by
these finite checks. No central map/manuscript or frozen run artifact is edited.
