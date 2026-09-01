# M206 exact cumulative-slack ladder reduction

Date: 2026-08-13 UTC.

## 1. Scope and disposition

This note concerns only fresh right-heavy parents in the normalized full
unweighted reset excursion `F=H/q` of the auxiliary nonlazy
minimal-long-cycle parking projection. The project target remains uniform
fixed-length identity transposition words, with `(pq)(x)=p(q(x))` and
displayed factors left-to-right.

The universal joint all-height inequality remains **unresolved**. The proved
output is a strict slack-ladder reduction:

1. the exact signed accounting identity is fixed before any bound;
2. every suffix-zero `B=2` actual-history feature vanishes, so fresh `B=2`
   parents have `T_h1=0` for all `L`;
3. at `(B,L)=(2,4)`, the unused `h=1` slack alone pays the reset/`h>=4`
   excess; and
4. at `(B,L)=(3,4)`, that terminal-only transfer fails exactly, while the
   cumulative `h=1,2` slack pays with a positive exact margin.

Thus a universal proof cannot stop at terminal unused slack. The `h=1,2`
finite pass is not promoted to a universal theorem. No tail bound, all-state
contraction, total AMV, gap, mixing, or Terminal statement follows.

## 2. Exact accounting and signs

For a fresh parent `xi_(B,L)=(B+L,2,1,B)`, write the exact actual-history
first-Jacobi charge as

```text
T_1(xi)=T_reset+sum_(h=1)^L T_h.                  (2.1)
```

The additivity is exact because reset and every `(d,t,a)` history branch are
orthogonal summands. Each `T_h` nevertheless retains the complete
Hilbert-valued child polynomial, every likelihood-weighted moment and cross
term, the parent covariance subtraction, and only retained `a<d`.

Let `U_1,U_2,U_3` be exactly the compatible same-parent accepted bounds from
M173/M177, M179/M184, and M193/M197, including their boundary cases. Put

```text
Delta=1-q-U_1-U_2-U_3,                           (2.2)
S_h=U_h-T_h,                         h=1,2,3,     (2.3)
X=T_reset+sum_(h=4)^L T_h-Delta.                  (2.4)
```

The accepted sector theorems give `S_h>=0`. Direct substitution, with no
inequality, gives the master identity

```text
(1-q)-T_1 = S_1+S_2+S_3-X.                       (2.5)
```

Consequently the surviving joint lemma is exactly

```text
X<=S_1+S_2+S_3.                                  (2.6)
```

The sign convention matters: positive `X` is the reset/high-tail amount not
covered by the nominal residual, while positive `S_h` is unused accepted
lower-height budget. Equation (2.5) also shows there is no literal
cross-sector Gram cancellation to discover—the sectors are orthogonal. Any
amortization is a transfer of nonnegative budget residuals.

For bookkeeping define cumulative slack

```text
C_k=sum_(h=1)^k S_h,                  k=1,2,3.    (2.7)
```

The question is at which rung `C_k` first dominates `X`; no fixed rung below
three is assumed universally.

## 3. Universal suffix-zero annihilation at B=2

Every fresh `B=2` height-one branch has `t=B+1=3`, hence child total
`s'=t-1=2` and bottom `B=2`; its beta parameters may depend on `(d,a)`.

> **Lemma 3.1 (proved).** For every valid `kappa,D`, the actual-history
> feature of `(s,kappa,D,B)=(2,kappa,D,2)` is identically zero.

**Proof.** The ordered compositions of two are `(2)` and `(1,1)`. No root is
live because its last part is at most `B=2`. The length-one composition has
no reset cut. The only cut of `(1,1)` has activity score

```text
1+1-1=1<2,
```

so it creates no active canonical reset endpoint. Thus both the reset and
descendant summands of the recursive Hilbert space are empty, whence
`Phi=0`. The argument is independent of `kappa,D`. QED.

Therefore, for every fresh `B=2` parent and every `L>=1`,

```text
T_h1=0,                 S_1=U_1.                  (3.1)
```

This is actual-history annihilation, not a scalar or operator-envelope bound.
It does not imply that `U_1` is itself history energy: when `U_1>0`, it is
pure unused envelope slack above the zero actual feature.

## 4. Decisive B=2,L=4 payment

The accepted M201/M204 row has

```text
U_1=S_1=3299/56250,
X=480024264873449410111/8339940489100500000000.
```

Exact subtraction gives

```text
C_1-X=S_1-X
=9103978211751469889/8339940489100500000000
>0.                                                     (4.1)
```

Thus the terminal unused slack alone pays the reset plus `h=4` excess in the
minimal M201 witness. Since `S_2,S_3>=0`, (2.5) then proves positive true
slack at this row. This resolves the *accounting* of the decisive witness;
it does not establish a uniform terminal-only transfer.

## 5. Exact adjacent obstruction at B=3,L=4

At the adjacent fresh parent, the exact compatible quantities are

```text
q=39375/262144,
U_1=23093/300000,       U_2=24/125,       U_3=27/125,
Delta=896580719/2457600000.
```

The exact literal-composition history recursion gives

```text
T_h1=3299/128000,
T_h2=1091287163/39375000000,
T_h3=108582539519/2835000000000,

T_reset=174263554388922831263/487049291366400000000,
T_h4=16843312139080279639/171603713767500000000.
```

Hence

```text
S_1=491551/9600000,
S_2=6468712837/39375000000,

X=134327445855119520136702145363
  /1474064677007114895360000000000.
```

Terminal-only payment fails by the exact amount

```text
C_1-X
=-58850574391835735352420545363
  /1474064677007114895360000000000
<0.                                                     (5.1)
```

This is a counterexample to the universal claim `X<=S_1`. It is not a
contraction counterexample. The next cumulative rung succeeds:

```text
C_2-X
=183315802718619702462160882861
  /1474064677007114895360000000000
>0.                                                     (5.2)
```

The full true slack, including `S_3`, is

```text
(1-q)-T_1
=445256035370256335108738960557
  /1474064677007114895360000000000
>0.                                                     (5.3)
```

Equation (5.2) is one exact finite row. It does not prove `X<=C_2` at any
other parent.

## 6. Structural obstruction to a literal feature transfer

Because (2.1) is an orthogonal direct sum, there are no omitted cross-sector
inner products whose sign could cancel reset/high-tail charge. Moreover,
Lemma 3.1 gives an actual zero `h=1` feature at `B=2` while (4.1) uses the
strictly positive upper-envelope residual `U_1`. Therefore any proposed
nonnegative transfer that is only a homogeneous functional of the actual
terminal feature must vanish in the decisive row and cannot explain its
positive payment.

A viable proof must couple the *residual of the accepted sector inequality*,
not merely transport an actual lower-sector vector. This sharply separates
the required budget certificate from a nonexistent Gram cross term.

## 7. Surviving standalone lemma

> **Cumulative lower-height unused-slack dominates reset/higher-tail
> (unresolved).** For every fresh parent, prove directly from the actual
> vector-history recursion and the residual certificates behind the accepted
> sector inequalities that
>
> ```text
> X(B,L)<=C_3(B,L)=sum_(h=1)^3 [U_h(B,L)-T_h(B,L)].
> ```
>
> Equivalently, construct a recursive certificate for (2.5) whose cumulative
> rungs may depend on the parent. It must retain observation dependence, all
> Jacobi modes and cross terms, and killed `a=d`.

The exact obstruction (5.1) proves that a universal certificate stopping at
`C_1` is impossible. The exact pass (5.2) is a useful base row only; `C_2`
is not conjectured universally without an analytic proof.

## 8. Reproducibility and limitations

Run

```text
python3 -B slack_ladder_exact.py --output slack_ladder_results.json
```

The script uses standard-library `Fraction`, `seed=null`, verifies the frozen
M204 literal-composition checker hash before importing it, and evaluates only
the named rows `B=2,L=4` and `B=3,L=4`. M204 already passed an immutable fresh
audit. A new referee should reconstruct both rows without importing M204.
