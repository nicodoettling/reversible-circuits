# M299 Checkpoint

## Pre-inspection initialization

Status: initialized before opening any M296 artifact.

The governing project files and sampler skill have been read.  No claim from
M296 has yet been inspected or adopted.  The fresh audit will reconstruct all
group-action and coset orientations from first principles, verify the frozen
hash/inventory before reading substantive files, and keep SSTID plus all
downstream mixing claims explicitly unresolved.

Planned decisive checks are the chronological residualization, transporter
and double-coset algebra, short stabilizer loops, and the distinction between
polynomial representative length and exponentially many indexed Schreier
generators.

## Halfway audit state

Status: immutable and dependency gates complete; core algebra reconstructed
through the pairwise and coset formulas.

- M296's top digest reproduces exactly as
  `9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f`.
  Its directory has exactly the seven manifest payloads plus `SHA256SUMS`,
  and every payload row passes.
- The eight cited frozen predecessor top digests reproduce exactly:
  M112 `43b5255f...f9cb3`, M119 `1fa3bddc...66a8`, M135
  `8d7ca3af...5358`, M137 `47dfb3f8...1af5`, M284
  `3176a4b1...62f3`, M288 `fd4120e2...2ca`, M291
  `cc60538b...c4b0`, and M294 `64f2e330...333a`. All 60 payload rows
  pass. M13's two pre-freeze proof hashes also reproduce.
- Semantic inspection confirms the exact imported scope: M13 supplies only
  individual signed-Hurwitz routes of length `50Nm^3`; rooted DPS gives the
  exact `d`-to-one quotient and `|Z_d|=d^(d-3)(2d-2)!`; M135/M137 supplies
  free `G,H` actions and actual perfect-matching-selected `H`-orbit edges;
  M284/M288 is chart-local word-level lifting only; and M291/M294 supplies
  separate frames and intrinsic framed fibers while explicitly leaving
  stabilizer cancellation open.
- From `beta=alpha_0;s;delta_0^(-1)`, direct chronological substitution gives
  the residual condition `L_Q;s;R_Q in S`, with
  `L_Q=alpha_Q^(-1);alpha_0` and
  `R_Q=delta_0^(-1);delta_Q`. Acting on `c` gives exactly
  `(c^L_Q)^s=c^(R_Q^(-1))`.
- Direct group algebra gives
  `C_Q != empty iff S;L_Q;S=S;R_Q^(-1);S`, and a chosen
  `s_Q in C_Q` gives both orientations
  `C_Q=Stab_S(x_Q);s_Q=s_Q;Stab_S(y_Q)`, with
  `Stab_S(y_Q)=S intersect R_Q;S;R_Q^(-1)`.

No material objection has appeared so far. Remaining checks before freezing
are frame covariance, finite-action lifting, the local loops and block swap,
the literal Schreier telescope/count, length equivalence, and the exact SSTID
stopping line.
