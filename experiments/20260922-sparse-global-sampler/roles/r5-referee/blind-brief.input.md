# Blind Brief: Sparse Global Identity-Bridge Sampling

Work initially from the definitions and candidate statements here, without
reading the coordinator's full prompt, other roles, previous project proofs
or verdicts. This is an open research target, not an assertion that a proof
has been found. Repository safety instructions still apply.

## Objects and Target T0

For N>=2 let T_N be all transpositions of S_N and

```text
Omega(N,m) = {ordered words w in T_N^m: product(w)=id}.
U_(N,m) = Unif(Omega(N,m)).
```

Labels and positions are distinguished. Compose permutations by
(alpha beta)(x)=alpha(beta(x)); rightmost factor acts first.

Investigate an expected-poly(N,m) bit-time algorithm which always outputs
a member of Omega(N,m) and satisfies, for EVERY even m>=0 with m^5<=N^3,

```text
TV(Q_(N,m),U_(N,m)) <= eta(N),
eta(N) <= N^(-a) eventually for each fixed a>0.
```

The bound and algorithm must be uniform over the stated lengths, and the
same algorithm must work for every a. Seek an explicit effective error
bound, including finite exceptions. Exact uniform sampling would suffice.
Fixed inverse-polynomial error or mere o(1) is weaker than this target.
No tunable error claim at fixed N,m is stipulated. Complexity is in N,
not log_2 N. Treat N=1, N=2, m=0, m=2 and odd lengths explicitly.

## A Specific Tail Statement to Test Independently

The support graph uses an edge for every transposition that occurs. A
nontrivial connected component on v vertices and ell factors has
ell=2v-2+2g, where g>=0 is an integer. Isolates have (v,ell)=(1,0).
Connected does not mean complete, and repeated edges are allowed.

```text
K(N,m)=max{1<=v<=N: v^(2v)<=(N+m+2)^4}.
A(N,m)={w in Omega(N,m): each nontrivial component has
        g<=1 or v<=K(N,m)}.
```

Assess the proposed statement that

```text
sup_{even m>=0, m^5<=N^3} Pr_{w~U_(N,m)}[w not in A(N,m)]
```

is negligible in N. The threshold is fixed from top-level N,m. Small
components of every feasible length/genus are included. Prove a bound,
refute this particular statement, or isolate the exact missing estimate.
Failure of this restriction is not a hardness result for T0.

## Permitted Sources and Review Tasks

Targeted primary-source checks are permitted, including:

- https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf
- https://math.stanford.edu/~vakil/files/g01hurwitz.pdf
- https://arxiv.org/pdf/2206.11315

Check normalizations, conditioning and asymptotic regimes from the source.
Do not infer identity-bridge independence from an ordinary random graph.
Exact finite checks can refute a bound but cannot prove negligibility.
Record complete inputs and whether context isolation was actually achieved.

Freeze blind_report.md by elapsed 90 minutes, then receive the candidate
proof and implementation for a current-version nonauthor audit. Do not
inspect previous verdicts or other workers' files until the blind phase ends.

## Operations

Model gpt-6-astra, effort ultra, no subagents or native goal creation.
Own experiments/20260922-sparse-global-sampler/roles/r5-referee/ only.
Use python3 -B, existing dependencies, bounded computations and exact tests.
No installs, escalations, system/config changes, commits, pushes or detached
work. Respect the absolute external deadlines supplied by the coordinator.
Checkpoint at least every 15 minutes. The four-hour cap covers the whole team.
