# M336 independent proof audit

Date: 2026-08-14 UTC

Fix only `k=9,n=27,H_2`, cell `(1,1)`, and
`Sigma={0,1,8,18,26}`.

The original A atom is channel 2, split 1,
`e=(3,4),f=(4,5)`, slot 1, owner size 1, profile `P=0`, empty
owner support, heads `{2,3,4}`, and raw mass
`117649/330024861>0`. The B atom is channel 2, split 1,
`e=(3,4),f=(4,6)`, slot 2, owner size 2, profile
`Q=(-1,0,...,0,1)`, owner support `{4}`, heads `{2,3,5}`, and
raw mass `7937147732541440/65835730184725763239>0`.

All owner/head sets miss `Sigma`. The opposite-source keys exist with
positive raw masses

```text
sigma(eta_B)_A = 224/1358127,
sigma(xi_A)_B  = 19461950683593750/65835730184725763239.
```

Product and slot determine the owner/head data, so switched Touch predicates
remain false. Opposite-key existence makes original `BadPref` false, and
the original key supplies each switched return prefix, so switched
`BadPref` is also false. Original and switched raw pairs are outside
`Exc_pf^*`.

Within each source every literal key
`(first edge,second edge,slot,product)` is unique. Switching sources on a
key present in both and switching back is therefore identity. This proves a
raw-label involution preserving the unordered profile pair and exception
predicate. It does not prove landing in the residual token measure.

The original factors are

```text
c_H=62/23
pi_11=72057594037927936/168377826559400929
rho_11=2354028198661286694240715/102166958637249138505285632
a_11(P)=583013693948397585119897/34055652879083046168428544
b_11(Q)=3296284725931531/9493588014497005568
u_A=20841167403/73338099464768
u_B=198428693313536/6311626321257167.
```

Their token weight is exactly

```text
425758390993809446972368496973627659814865534216945520778179328
/160127614349801894448349798657905382956928144305646616084388152620616845
>0.
```

Both switched splits remain 1, so the reverse cell is still `(1,1)`.
But `a=[g-f]_+` and `b=[f-g]_+` have disjoint support in every fixed
cell. Thus `a_11(P)>0,b_11(Q)>0` force exactly
`b_11(P)=0,a_11(Q)=0`. The reversed residual token is absent and the
compatible landing clause fails before any weight ratio is defined. Raw-label
involutivity cannot cancel compatible residual flux.

On the original token universe, indicators of `Exc_pf^*` and its complement
partition every token, so before absolute values
`J=J_compatible+J_exceptional` exactly. This is bookkeeping, not
cancellation.

For endpoint exception probabilities, the union bound and exact token
marginals give

```text
mass(Exc_pf^*) <= c_X sum_(s,t) pi_st [
 sum_P a_st(P)epsilon_A(s,P)+sum_Q b_st(Q)epsilon_B(t,Q)].
```

Using `a<=g,b<=f` and the `pi` marginals gives
`c_X[sum_s q_s E_A(s)+sum_t p_t E_B(t)]`. Substitution of the locked
Borel laws
`q_s=k/(k-1)b_sR_k(s)` and
`p_t=(2k-1)/(2k-2)b_tR_(2k-1)(t)` is exactly M335's scalar reduction.
It proves no H/A/C endpoint estimate. Those scales remain open and would
control only `J_exceptional`, not the uncancelled compatible flux.

No alternate surgery, new rank/cell, MPCF statement, or downstream inference
is made.
