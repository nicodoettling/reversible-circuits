# M81 plan: fresh referee of M78 voltage obstruction

Date: 2026-08-12

## Objective and scope

Independently referee the frozen M78 report at SHA-256
`c6b0e36ef09608e3fe962e0d85ad572db02b756726a8128548738473855576e1`.
The global target remains the uniform fixed-length law on
`Omega(N,m)`, and the literal chain remains the lazy exact same-product
`{3,4,5}` heat bath.  This mission audits only the canonical positive-Hurwitz
row construction in the two-component near-minimal reduction; it cannot by
itself establish Terminal B.

Permutations use `(pq)(x)=p(q(x))`, factors are written left-to-right, and the
right Hurwitz move is `(a,b) -> (b,bab)`.

## Claim under test

For M78's explicit `Z_L^2` voltage-lift word `W_L`, every `L>=2` gives a
connected, simple, bipartite genus-one identity word with no safe canonical
elimination prefix through depth two.  Separately audit the elimination law,
safe-prefix equivalence, finite counts, and every all-`L` voltage and
connectivity assertion.

## Independent checks

1. Verify hashes and immutability of every M78 artifact.
2. Derive the elimination/conjugation formula and safe-prefix equivalence.
3. Reimplement all decisive finite checks without importing M78 code.
4. Prove the four-transposition collision classification for a simple
   triangle-free support.
5. Enumerate all 36 base `K_(4,4)` four-cycles symbolically, including exact
   integer voltage vectors, and identify the eight zero-voltage cycles.
6. Prove identity from lifted token trajectories, connectedness from voltage
   generators, and simplicity/bipartiteness/genus for every `L>=2`.
7. Check every collision order on the eight zero cycles and prove why lifted
   deletion disconnects for all fibers and moduli.
8. Give an `ACCEPT` or `REJECT` decision with numbered objections.
9. Continue on the total-prefix incidence `eta_L`, seeking a rigorous
   homological characterization or asymptotic bound while retaining the
   canonical-law-only scope warning.

## Expected failure modes

- a nonzero integer base voltage may vanish modulo `L=2`;
- a lifted four-cycle may project to an overlooked reduced base walk;
- a collision order may be safe in one fiber despite being unsafe in the
  base graph;
- later conjugations may invalidate a naive support-cycle characterization;
- absence of bounded-depth hits may say nothing about total row probability.

Exact checks use standard-library Python, no random seed, and record the
repository commit and Python version.  Any exploratory stochastic check will
use an explicit fixed seed and remain labeled empirical.
