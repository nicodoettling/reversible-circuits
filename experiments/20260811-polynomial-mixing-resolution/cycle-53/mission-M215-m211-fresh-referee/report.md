# M215 report: fresh immutable referee of M211

Date: 2026-08-13 UTC.

## 1. Verdict and scope

ACCEPT M211'S REFUTATION OF POINTWISE IKBE-b AND THEREFORE OF THE
TWO-CLAUSE IKBE CONJUNCTION.

Material objections: none. IKBE-a/DV, signed averaged DE, conditional J=2,
and every downstream claim remain open.

## 2. Immutable gate

All eight M211 entries pass sha256sum -c SHA256SUMS. Fresh hashes agree;
M211's checksum-file digest is
79f3e0f614a6cde4e3e4bd36ce55e217b35416f68470c6deab93598877874225.
M211 was never edited.

## 3. Target and convention

Target: normalized literal disjoint ordered-double B/A profile laws under
uniform minimal factorizations in the fixed-cell coordinate calculation,
n=3k, odd k>=3. Composition is (pq)(x)=p(q(x)); displayed factors are
left-to-right. Observable: the one-run prefix Y_l.

## 4. Exact witness and seam values

For k=12q-1,s=3q,l=4q, all parameters are admissible. Independent seam
counting gives

    F_l(s)=1-s/(2k-1), F_l(2k-1-s)=0,
    J_l(s)=1-s/k,     J_l(k-s)=0.

## 5. Critical-Borel certificate

The rooted-tree equation at z=e^-1 gives sum_d b_d=1 and
beta=sum_(d>=2)b_d=1-e^-1. Uniform Stirling bounds split the W_r tail into
M<d<=r/2, bounded by O(M^-1/2), and d>r/2, bounded after c=r-d by
O(k^-1/2). Hence W_(rho k)->rho beta/2. The A fresh term tends beta/2.

## 6. Exact limiting defect

The B kernel terms tend beta/8+7beta/8=beta. The A terms tend
beta/8+3beta/8+beta/2=beta. Both normalizers tend one. Surviving faces tend
49/64 on B and 42/64 on A, so

    Phi_(3q)^D(Y_(4q))-Psi_(3q)^D(Y_(4q))->7/64.

Since sqrt(4q)/(12q-1)->0, pointwise IKBE-b is false.

## 7. Exact scope

Because IKBE-b is one conjunct, the two-clause IKBE lemma is false.
This does not touch IKBE-a/DV. It also does not refute signed averaged DE:
the pointwise witness omits q_hat weighting and possible signed cancellation
across first splits.

## 8. Calibration and objections

An independent formula-only q=1 checker imports no M211 code/data. At
(k,s,l)=(11,3,4) it reproduces the exact rational defect, approximately
0.09224121091748724. This is finite calibration only.

Numbered objections:

1. Nonmaterial: state c<r/2 explicitly after the complementary-tail
   substitution in M211's proof.
2. Nonmaterial: mention T=ze^T at z=e^-1 to make beta=1-e^-1
   self-contained.

## 9. Artifacts and action

Artifacts: plan/checkpoint, proof audit, clean-room checker/output, results,
report, and freeze files. Python 3.12.3, standard library, seed null.
Action: freeze ACCEPT and request a fresh immutable audit. Preserve the exact
scope; pursue IKBE-a/DV and signed averaged DE separately.
