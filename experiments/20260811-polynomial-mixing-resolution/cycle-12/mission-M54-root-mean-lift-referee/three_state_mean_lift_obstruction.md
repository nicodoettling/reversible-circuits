# Three-state obstruction to an abstract mean-lift shortcut

Let the reversible law be uniform on `{a,b_1,b_2}`. Give the undirected
edge `a--b_1` stationary capacity `q/3` and `b_1--b_2` capacity
`epsilon/3`, with `0<epsilon,q` small enough that diagonal holding makes a
Markov kernel. Partition the states into `{a}` and `{b_1,b_2}`.

The crossing source on `{a}` is its stationary conditional law. The
crossing target is the point mass at `b_1`, whose density relative to the
uniform conditional law on `{b_1,b_2}` is at most two. Thus one-sided
exact lumping and a constant target Radon--Nikodym bound both hold.

For `f(a)=f(b_1)=0` and `f(b_2)=1`, the fibre means are `0` and `1/2`.
Using undirected capacities,

```text
E_quotient(E[f|fibre])=(q/3)(1/2)^2=q/12,
E_full(f)=(epsilon/3)(1-0)^2=epsilon/3.
```

Their ratio is `q/(4 epsilon)`, which is unbounded. Hence bounded target
density plus exact source marginal does not by itself imply a mean-lift
inequality. This construction refutes only that abstract inference. It is
not a counterexample to the geometrically structured parking chain.
