# M207 clean-room proof audit of immutable M199

Date: 2026-08-13 UTC.

Status: ACCEPT M199's strict exact literal-profile reduction. This audit
does not prove IKBE, DV, DE, the conditional J=2 prefix estimate, or any
downstream claim.

## 1. Immutable gate

Every file named by M199's SHA256SUMS passed sha256sum -c before its
contents were used. Fresh hashes agree with the frozen manifest. M199 was
not edited.

## 2. Per-placement completion law

For residual component sizes d_i and total rank R, the number of ordered
minimal completions is

    F_R = R! product_i tau(d_i).

After the first exterior factor the rank is

    R_* = (2k-2)-1 = 2k-3.

If a fixed second edge cuts a post-first component of size r into d and
r-d, its conditional completion ratio is therefore

    F_(R_*-1)(post-second) / F_(R_*)(post-first)
      = tau(d)tau(r-d) / [R_* tau(r)]
      = b_d b_(r-d) / [R_* b_r].

Thus M199's denominator is 2k-3, not 2k-2 or 2k-4. Summing over every
internal second edge gives one by the first-factor decomposition of
minimal completions.

## 3. Literal B tuple law and faces

Put D=2k-1 and V=(1,...,k-1,2k,...,3k-1). For a fixed smaller first split
s, a tuple (i,r,d,a) has

    r in {s,D-s},  1 <= d < r,  1 <= a <= r-d-1.

It denotes first edge {v_i,v_(i+r)} and second edge
{v_(i+a),v_(i+a+d)}. Each first chord appears in the two r branches once
per active post-first piece. A disjoint second edge lies in exactly one
piece, so the complete tuple, hence each ordered disjoint pair, occurs
exactly once. The outer factor is consequently 1/D, not 1/(2D).

The complementary first piece gives directed ambient gap

    g_1 = v_i-v_(i+r) mod 3k,

and the second cut gives

    g_2 = v_(i+a+d)-v_(i+a) mod 3k.

These are exactly the two one-run faces. Four distinct chord endpoints
leave the third face with two ambient runs and size 3k-g_1-g_2. This
rederives both B-Y and B-X, including multiplicity when face atoms coincide.

For x<k, an x-step source arc crosses neither seam at D-2x starts and each
of the two seams at x starts. Its gaps are respectively x, x+1, and x+k.
For x>=k, complementing the c=D-x step gives gaps 3k-c, 3k-c-1, and
3k-c-k with multiplicities D-2c,c,c. These are exactly M199 (2.5a,b).

## 4. Literal A law and untouched mass

There are 2k first A chords of a fixed smaller split s: k in each
contiguous k-cycle. They have equal completion weight. After one is chosen,
the marked pieces have sizes s and k-s and the other k-cycle is untouched.
The sum of second-edge completion ratios inside any component equals its
rank divided by total residual rank. Hence the untouched component has raw
mass

    u_k = (k-1)/(2k-3).

In a marked component of size r, deleting the two shared-endpoint
possibilities leaves raw mass

    h_*(r) = (r-1)(r-2)/[r(2k-3)].

Partitioning by marked versus untouched parent gives A-full. Averaging
contiguous placements gives J_l(x)=(k-x)/k on the cutoff and yields A-Y,
including C_l. The literal A-full formula supplies the complementary
two-run atom for X without an implicit orientation.

## 5. Shared endpoints, kinds, and collisions

The B offset condition excludes the marked start of each active piece.
Across the two r branches it therefore removes exactly all, and only,
second edges sharing a first-edge endpoint. The A marked-piece domains do
the same; an edge in the untouched k-cycle cannot share a first endpoint.
Their deleted masses rederive gamma_L(s) and gamma_F(s).

No absolute kind split occurs. The literal tuple support contains every
same/same, same/cross, cross/same, and cross/cross B stratum. Each face is
added as an atom rather than converted to a set, so equal-size and
equal-run-type collisions retain multiplicity.

## 6. Exact four-part adjacent-split map

For a piece of size r write

    T_r = {(d,a): d>=1, a>=1, a+d<=r-1}.

Under s to s+1, the common short tuples are T_s and the added short tuples
are exactly

    {(d,s-d): 1<=d<s}.

The common long tuples are T_(D-s-1), and the tuples deleted from the old
long interval are exactly

    {(d,D-s-1-d): 1<=d<D-s-1}.

For every common tuple, only the parent size r changes by one. This changes
the kernel K_*(r,d) and the ambient gap whose parent endpoint moves; for X
the complementary two-run indicator changes with those same gaps. The
outer 1/D is fixed. Finally the conditional scalar changes from
1/[1-gamma_L(s)] to 1/[1-gamma_L(s+1)]. These are precisely M199's four
parts, and the domains show there is no fifth support edit.

## 7. Exact implication of IKBE

IKBE-a is word-for-word DV after setting Z_l^B(s)=Phi_s^D(Z).
Pointwise IKBE-b gives

    |sum_s q_hat_s(Phi_s^D-Psi_s^D)|
      <= sum_s q_hat_s C sqrt(l)/k
      <= C sqrt(l)/k,

because q_hat is a subprobability measure. Thus it implies DE while keeping
the signed channels combined inside each profile.

Together with the already accepted M192 Abel identity and
|E_u|<=C sqrt(u)/k, DV bounds the variation term by C sqrt(l)/k. M192's
endpoint is O(k^-2) and its shared-endpoint term is O(k^-1). Therefore
IKBE would imply only the conditional J=2 prefix estimate. It does not by
itself prove PCR, WPCR, SCBR, or any downstream claim.

## 8. Exact falsification check

The independent standard-library checker uses only k=3,5. It derives
completion ratios directly, compares the B tuple support with literal
ordered pairs, checks every literal face against the gap formula, verifies
both seam laws, checks gamma deletion and the A untouched mass, reconstructs
A-Y, retains kind strata and collision multiplicities, and checks the
adjacent tuple domains. All 649 recorded assertions pass. This is finite
falsification only, not evidence for IKBE.

## 9. Objections and verdict

Material objections: none.

Numbered nonmaterial qualifications:

1. M199 Section 4 states the four-part map tersely. Writing the explicit
   T_r domains above makes clear that the seam edit also includes the
   complementary X face; no mathematical correction is needed.
2. The phrase that IKBE yields the conditional J=2 estimate must be read
   with M192's accepted Abel identity, cumulative bound, endpoint, and
   shared-endpoint estimate. M199 does so contextually; IKBE alone is not a
   standalone J=2 theorem.

Verdict: ACCEPT the strict exact reduction. Keep IKBE, DV, DE, conditional
J=2, PCR/WPCR, SCBR/BIR/BR/PCS, and every downstream statement open.
