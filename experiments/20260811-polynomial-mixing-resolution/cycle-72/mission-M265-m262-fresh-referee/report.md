# M265 Final Report: Fresh Referee of M262

## Verdict

```text
ACCEPT M262'S ARBITRARY-RANK CPR COUNTERFAMILY.
RETAIN M257/M260 CP-1--CP-6.
```

Material objections: none.

For every `rho>=8`, M262's graph is an admissible tree rooted at the leaf
`rho`, with stopped path `4 -> 6 -> 1`, no rooted child of `4`, and hence
`E_4={6}`.  Literal CP-5 insertion into CP-2 at the strict nonroot vertex
`a=6` uses the essential incidence `kappa(4)=L_4=5`.  The complete-node
deletion order exposes

```text
W_6^6 S B_6^6 -> S,
```

so the only exposed label has distance one rather than CPR's required
distance three.  The residual is the rank-stable open frontier

```text
S S B_4^9 B_4^8 B_4^7 S
W_4^7 W_4^8 W_4^9 W_4^10 S S.
```

Passing from `rho` to `rho+1` inserts only the two new modulus labels into
the two distance-one deletion chains.  They disappear before the same
low-label residual is reached.  This is a symbolic interval argument; the
independent `rho=8,9` guard only checks indexing and boundary behavior.

The family directly refutes M250 `(4.2)` / M257 CPR's first-above-`v`
`O -> C` clause.  It does not enter the `a=1` root row.  Thus it does not
refute the raw CP contexts, the root endpoint identities themselves, or IDL.
It does show that a bare `O/C` tag is not currently a justified sufficient
input description for RST: the literal incoming frontier or a proved refined
quotient is required.  `O^- / O^+` is a necessary first distinction, not a
proved sufficient state space.

Numbered qualifications:

1. No material objection.
2. Nonmaterial N-1: under-specification of `O/C` is not a counterexample to
   endpoint tables `(4.4)--(4.5)`.
3. Nonmaterial N-2: M262 does not, and must not, promote `O^- / O^+` as
   already sufficient.

The full audit and dependency hashes are in `proof_audit.md`.  No routing,
gap, mixing, or Terminal inference is made.

