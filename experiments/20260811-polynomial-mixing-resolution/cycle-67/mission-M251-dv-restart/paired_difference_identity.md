# M251 exact paired-domain adjacent-split identity

Date: 2026-08-14 UTC.

Status: the identity below is **proved algebraically** from the accepted
M199/M207 literal tuple law.  No estimate labelled `(DV)` is claimed here.

## 1. Literal profile and notation

Fix odd `k >= 3`, put

```text
n=3k,                 D=2k-1,                 R=D-2=2k-3,
b_j=e^-j j^(j-1)/j!,  K(r,d)=b_d b_(r-d)/(R b_r).
```

Let `V=(v_0,...,v_(D-1))=(1,...,k-1,2k,...,3k-1)` cyclically, and write

```text
A(i,x)=v_(i+x)-v_i mod n,
I_l(i,x)=1{2<=A(i,x)<=l},
F_l(x)=D^-1 sum_i I_l(i,x).
```

For `Z=Y_l,X_l`, remove the surviving complementary one-run face from the
literal tuple observable and put

```text
c_r^Y(i,d,a)=I_l(i+a,d),

c_r^X(i,d,a)=I_l(i+a,d)
 +1{2<=n-A(i+r,D-r)-A(i+a,d)<=l}.                  (1.1)
```

Define

```text
h(r)=(r-1)(r-2)/(rR),

V_r^Z=D^-1 sum_i sum_(d=1)^(r-2) K(r,d)
                    sum_(a=1)^(r-d-1)c_r^Z(i,d,a),

U_r^Z=h(r)F_l(D-r)+V_r^Z.                          (1.2)
```

All empty sums are zero.  M199/M207's literal formula is exactly

```text
N_s^Z=U_s^Z+U_(D-s)^Z,
H_s=h(s)+h(D-s)=1-gamma_L(s),
Phi_s^D(Z)=N_s^Z/H_s.                              (1.3)
```

For `Y`, (1.2) is the accepted closed formula

```text
V_r^Y=sum_(d=1)^(r-2)(r-d-1)K(r,d)F_l(d).
```

For `X`, (1.1) retains the complementary two-run atom literally, including
all seam incidences and repeated-size multiplicity.

## 2. One-parent expansion on a common triangular domain

For `1<=r<=D-2`, set `delta V_r^Z=V_(r+1)^Z-V_r^Z`.  The old and new
triangular tuple domains have the common part

```text
1<=d<=r-2,             1<=a<=r-d-1,
```

and the new boundary strip

```text
1<=d<=r-1,             a=r-d.
```

Consequently the following identity is exact:

```text
delta V_r^Z = C_r^Z + E_r^Z + B_r^Z,               (2.1)

C_r^Z = D^-1 sum_i sum_(d=1)^(r-2) sum_(a=1)^(r-d-1)
          [K(r+1,d)-K(r,d)] c_r^Z(i,d,a),

E_r^Z = D^-1 sum_i sum_(d=1)^(r-2) sum_(a=1)^(r-d-1)
          K(r+1,d)[c_(r+1)^Z(i,d,a)-c_r^Z(i,d,a)],

B_r^Z = D^-1 sum_i sum_(d=1)^(r-1)
          K(r+1,d)c_(r+1)^Z(i,d,r-d).
```

Here `C` is the common-domain smooth kernel edit, `E` is the common-domain
seam/cutoff edit (`E_r^Y=0` identically), and `B` is the added boundary
strip.  No absolute value has been taken and no kind or collision stratum
has been separated.

The surviving-face part has the exact increment

```text
T_r := h(r+1)F_l(D-r-1)-h(r)F_l(D-r)
     = J_r+M_r,                                      (2.2)

J_r=h(r+1)[F_l(D-r-1)-F_l(D-r)],
M_r=[h(r+1)-h(r)]F_l(D-r).
```

Thus `J_r` isolates the literal prefix-cutoff jump and `M_r` is its smooth
mass edit.

## 3. Short/long paired split difference

Fix `1<=s<=k-2` and put `q=D-s`.  Since increasing the short piece from
`s` to `s+1` decreases the long piece from `q` to `q-1`, (1.2)--(2.2) give

```text
N_(s+1)^Z-N_s^Z
 = (J_s-J_(q-1)) + (M_s-M_(q-1))
 + (C_s^Z-C_(q-1)^Z)
 + (E_s^Z-E_(q-1)^Z)
 + (B_s^Z-B_(q-1)^Z).                              (3.1)
```

This is the required common-domain pairing: the short and long
fragmentation edits are combined *before* any absolute value.

The normalization difference is particularly transparent.  Since

```text
h(r)=(r-3+2/r)/R,
h(r+1)-h(r)=[1-2/(r(r+1))]/R,
```

the two leading `1/R` derivatives cancel exactly:

```text
H_(s+1)-H_s
 = [h(s+1)-h(s)]-[h(q)-h(q-1)]
 = (2/R)[1/((q-1)q)-1/(s(s+1))].                  (3.2)
```

Combining (3.1)--(3.2) with the quotient rule yields the exact adjacent
profile identity

```text
Phi_(s+1)^D(Z)-Phi_s^D(Z)
 = 1/H_(s+1) * {
      (J_s-J_(q-1)) + (M_s-M_(q-1))
     +(C_s^Z-C_(q-1)^Z)
     +(E_s^Z-E_(q-1)^Z)
     +(B_s^Z-B_(q-1)^Z)
     -Phi_s^D(Z)[H_(s+1)-H_s]
   }.                                               (3.3)
```

The five numerator blocks in (3.3) are, respectively, survivor/cutoff,
survivor smooth mass, common smooth kernel, common seam/cutoff, and
strip/boundary; the last term is the normalization block.

## 4. Explicit cancellation inside the paired boundary strip

The strip must also remain paired.  Put

```text
lambda_r(d)=b_(r-d)/b_r,
g_r^Z(d)=D^-1 sum_i c_r^Z(i,d,r-1-d).
```

Then `K(r,d)=b_d lambda_r(d)/R`.  With the harmless convention that a sum
over an empty range is zero, the strip pair in (3.1) is exactly

```text
B_s^Z-B_(q-1)^Z
 = 1/R sum_(d=1)^(s-1)b_d {
      [lambda_(s+1)(d)-lambda_q(d)]g_q^Z(d)
      +lambda_(s+1)(d)[g_(s+1)^Z(d)-g_q^Z(d)]
   }
   -1/R sum_(d=s)^(q-2)b_d lambda_q(d)g_q^Z(d).    (4.1)
```

For `Y`, `g_r^Y(d)=F_l(d)` is independent of `r`, so the second term in
braces vanishes identically.  Formula (4.1) then displays the cancellation
of the common leading boundary kernel `b_d/R`; only the likelihood-ratio
difference and the unmatched long cutoff tail survive.  For `X`, the same
kernel cancellation is exact, while the remaining difference of the two
literal boundary indicators is retained as a single paired seam/cutoff
term.  This is precisely why splitting short and long fragmentation laws in
absolute value would discard the needed cancellation.

## 5. Proof

Equation (1.3) is M199's accepted literal tuple formula after separating the
first complementary one-run indicator, whose tuple-weight sum is `h(r)`.
When `r` increases by one, the two triangular domains have exactly the
common part and strip displayed above.  On the common part add and subtract
`K(r+1,d)c_r^Z`; this proves (2.1).  Adding and subtracting
`h(r+1)F_l(D-r)` proves (2.2).  Since

```text
N_(s+1)-N_s=(U_(s+1)-U_s)-(U_q-U_(q-1)),
```

(3.1) follows.  The displayed formula for `h` proves (3.2), and ordinary
finite quotient algebra proves (3.3).  Finally split the `d`-domain of
`B_(q-1)` at `s-1`, substitute `K=b_d lambda/R`, and add and subtract
`lambda_(s+1)g_q`; this proves (4.1).

All identities are finite and valid at `s=1` and every empty-domain
boundary.  They use no asymptotics or finite experimental inference.

