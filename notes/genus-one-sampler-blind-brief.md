# Blind Referee Brief: Connected Identity Words

This is a research question, not an assertion that a proof is known. Work
from the definitions and permitted primary sources below. Until you save
your initial blind_report.md, do not read other workers' files, historical
research reports, or coordinator summaries. Repository safety instructions
still apply. Do not create a goal or spawn subagents.

## Frozen Target T0

For N>=2, let T_N be all transpositions of S_N. Define

```text
X_N = {w=(t_1,...,t_(2N)) in T_N^(2N) : product(w)=id,
       the graph on [N] with edges t_i is connected}.
```

Words are ordered and vertices are labeled. Repeated edges are allowed.
Connected does not mean complete. Composition is (a b)(x)=a(b(x)), so the
rightmost displayed factor acts first. The desired target is Unif(X_N).

Investigate whether, for every N>=2 and positive integer b, an algorithm
can return a word in X_N exactly with TV error <=2^(-b) in expected bit time
polynomial in N and b. An exact expected-polytime sampler is also acceptable.
You may use connected factorizations of arbitrary endpoints internally, but
must distinguish those from unconstrained endpoint bridges. Address N=2
(the unique transposition repeated four times), N=1 (infeasible), and N=3.

Attempt a construction or identify the exact mathematical obstacles. Test
count-to-sample reasoning, conditioning, endpoint and connectivity constraints,
representation multiplicities, and arithmetic complexity. Finite tests do
not prove an asymptotic theorem. Failure of one algorithm is not hardness.

## Permitted Primary Sources

These are candidate resources, not endorsed routes or assumed conclusions:

- https://math.stanford.edu/~vakil/files/g01hurwitz.pdf
- https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf
- https://arxiv.org/pdf/1410.6521
- https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf

Other targeted primary-source checks are permitted; record exactly what was
checked and its convention translation. Do not inspect prior project verdicts
until your blind report is complete. Record the full input you received and
whether the agent context actually excluded the coordinator's argument.

## Operational Limits

Model gpt-6-astra, reasoning effort ultra; no delegation. Own only
experiments/20260907-genus-one-sampler/roles/r3-referee/.
Workspace-write with approval_policy=never. No installs, escalations, system
changes, commit, push, or detached computation. Obey the absolute deadlines
provided by the coordinator from the external cap. Checkpoint every 15 minutes.
Deliver an initial blind report by elapsed 120 minutes, sooner if complete,
then await the candidate proof for a nonauthor audit within the same cap.
