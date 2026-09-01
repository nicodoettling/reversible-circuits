# Exact Stationary Adjacent-Square Frequency

Let `M=binom(N,2)`, let `P` be the simple random-transposition transition
operator on `S_N`, and write `p_m=P^m(id,id)`. Then

    |Omega(N,m)|=M^m p_m.

Fix an adjacent position pair `j,j+1`. Inserting `(t,t)` at that position is a
bijection

    Omega(N,m-2) x T_N
      -> {w in Omega(N,m):t_j=t_{j+1}}.

Therefore, under global uniform `pi_{N,m}`,

    Pr(t_j=t_{j+1})
      = M |Omega(N,m-2)| / |Omega(N,m)|
      = p_{m-2}/(M p_m).

For even `m`, spectral calculus for the self-adjoint contraction `P` gives

    p_m = integral lambda^m dmu_id(lambda)
        <= integral lambda^(m-2) dmu_id(lambda) = p_{m-2},

because `lambda^m<=lambda^(m-2)` on `[-1,1]` when both exponents are even.
Consequently

    Pr(t_j=t_{j+1}) >= 1/M.

The square label is exactly uniform on `T_N`, since deletion gives precisely
one shorter identity word for each label. Thus a stationary step of the
auxiliary pair heat bath `J` performs a changed square refresh with probability
at least

    (1/2) (1/M) (1-1/M),

after averaging over the uniformly selected adjacent position. This is
polynomially small in `N`, never superpolynomially small.

This lemma is an average stationary-flow fact. It does not say every word has
an adjacent square, does not control a particular macro cut, and does not by
itself give a gap lower bound. In the sparse regime `m<<M`, many individual
words may have no adjacent square even though each fixed position has the
stated stationary probability.
