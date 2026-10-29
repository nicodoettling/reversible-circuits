# C1 rejection v1: many surviving null windows

Status: PROVISIONAL proof; candidate verdict reject on its concrete lambda schedule, pending author-distinct review. This rejection was written before selecting C2. C1-v1 is immutable. No computation has yet run.

Let X(w) count the B disjoint aligned six-position windows of product identity. At the start X=B. One adjacent Hurwitz update touches at most two aligned windows. Each replacement touches one. Therefore, pointwise for every tape,

    X(Q_k(C1)) >= B-2s-k.

This argument deliberately overcounts damage; a move inside a block preserves its product. No independence of surviving windows is claimed.

Use the test E={X>=a}, where a=ceil(B/2). On the C1 schedule N=lambda^2, B=lambda^6, s=floor(B/10), k=lambda, lambda>=2, B-2s-k>=a, hence Pr_C1[E]=1.

For the matched reference, let V be an iid mu length-L word and F={product(V)=id}. Then U is V conditioned on F. Use the same independent exact Q_k channel in both calculations. Its output on V is still iid mu: condition on its replacement subset, and each coordinate is either its original independent uniform gate or a new independent uniform gate. Thus

    Pr[Q_k(U) in E] <= Pr[Q_k(V) in E]/Pr[F]
                      = Pr[V in E]/p_L(id).

Because L is even, p_L(id)=sum_g p_(L/2)(g)^2>=1/N! by Cauchy--Schwarz. In an iid word the B disjoint block-identity indicators are independent with probability p_6(id). Moreover p_6(id)<=p_2(id)=1/q, since convolution by a probability measure contracts the l2 norm: p_(2r)(id)=||p_r||_2^2. A union bound over subsets of a windows gives

    Pr[Q_k(U) in E] <= min(1, N! * binom(B,a) * q^(-a))
                    <= min(1, N! * 2^B * q^(-a)).

Consequently advantage is at least 1 minus that upper bound, with one sample and O(L) label operations for block evaluation (or O(L+N) array implementation). Reused-setup insecurity follows already from one sample; there is no key.

For the schedule, log of the latter bound is at most N log N + B log 2 -(B/2)log q = -Omega(lambda^6 log lambda). This is negligible in lambda, so advantage tends to one with superpolynomially small deficit. This is an asymptotic attack, not an inference from finite data. It applies at sparse k/L=lambda^(-5)/6 and common semantic error upper bound 4/lambda, which is not negligible.

Dependencies: exact C1 identity and product preservation; iid channel invariance; elementary l2 contraction and Cauchy--Schwarz; union bound. No imported mixing theorem, sampler theorem, or disconnected-vs-connected approximation. Probability audit: the ONLY product p_6^a is under the unconditioned iid gate law on fixed disjoint windows. No product bound is applied after conditioning on the bridge or on surviving construction windows. Conditioning is paid once by 1/p_L. The hidden Q_k subset is independent, as M0 requires.

Boundary checks: for k=L, the deterministic threshold premise fails and both laws are iid. For N=2 C1 is undefined; the inequality for reference still holds but is uninformative. L=0 is outside C1. For small B or s large the deterministic lower bound can be negative and gives no attack. Nothing here rejects all structured samplers or sufficiently aggressive scrambling.

Review provenance: the author had already independently frozen C1 before an unsolicited r1 message described a similar general surviving-window idea. This is therefore an author-distinct construction-side proof, not blind theory review. The present elementary reference counting argument was derived here. Same-model reasoning remains correlated.
