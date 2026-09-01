# M325 strongest surviving owner-specific lemma

Date: 2026-08-14 UTC
Status: exact identity and conditional implication proved; sign unresolved

## Active-owner truncated incidence identity (AOTI_1)

Keep the exact truncated measures and owner notation of
`candidate_frozen.md`, but project a full completion signature to the owners
actually hit by the two target boundary edges.  There are only two kinds:

```text
S_d       : both edges have the same owner of size d,
X_(d,e)   : the edges have distinct owners of sizes d<=e.    (1.1)
```

Let `M_T^+(S_d),M_T^-(S_d)` and
`M_T^+(X_(d,e)),M_T^-(X_(d,e))` be the rational masses obtained by summing
the corresponding indicators against `(p_T,n_T)`, every `k` middle phase,
and every target phase.  Define their signed differences by

```text
Delta_T^S(d)=M_T^+(S_d)-M_T^-(S_d),
Delta_T^X(d,e)=M_T^+(X_(d,e))-M_T^-(X_(d,e)).        (1.2)
```

With the actual rooted-tree ratios

```text
a_d=tau(d-1)/tau(d),       b_d=tau(d-2)/tau(d),      (1.3)
```

one has exactly, at every staircase endpoint and in fact at every rational
cutoff `0<=T<=mu_k`,

```text
Psi(T)
 =sum_(d>=3) b_d Delta_T^S(d)
  +sum_(2<=d<=e) a_d a_e Delta_T^X(d,e).             (AOTI_1)
```

Invalid or nongeneric terms are zero.  The lower bounds merely record that
a size-two owner cannot support two distinct generic boundary tails and a
singleton cannot support one.

### Proof

Expand every literal state response over target phase `x`.  A same-owner
term has coefficient `tau(d-2)/tau(d)=b_d`; a distinct-owner term has
coefficient `tau(d-1)tau(e-1)/(tau(d)tau(e))=a_da_e`.
Group first by `(1.1)`, then sum against the exact rational truncated source
measures.  This is precisely `(AOTI_1)`.  All inactive owners disappear
only because their completion ratio is `tau(d)/tau(d)=1`; no owner response
is approximated.  QED.

## Strictly weaker sufficient lemma left open

Full-profile domination in `TOEC_1` implies, after summing over inactive
owner data,

```text
Delta_T^S(d)>=0,          Delta_T^X(d,e)>=0           (AOEC_1)
```

for every active signature.  Hence `AOEC_1` together with `(AOTI_1)` would
imply `GQAC_1`.  The converse implication from full-profile domination is
strictly lost: the singleton obstruction is quotiented out before the
active masses are compared.

`AOEC_1` is only the next strictly weaker, actual-owner-specific standalone
obligation.  It is not asserted, tested, or replacement-searched here.  In
particular `(AOTI_1)` assigns no sign to an active signature and makes no
MON/FOSD, PSD, one-direction Abel, cell, block, or fixed-middle claim.

Lag reflection is literal: exchanging the ordered target phases identifies
the active tables at `ell` and `n-ell`.  The terminal cutoff gives the full
MCLP aggregate; canonical intermediate endpoints give the exact GQAC
prefixes.

