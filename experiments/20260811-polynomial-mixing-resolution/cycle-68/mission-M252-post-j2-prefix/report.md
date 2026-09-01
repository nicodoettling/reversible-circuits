# M252 report: post-J=2 prefix implication

Date: 2026-08-14 UTC.

Verdict: **conditional full WPCR proved; full PCR unresolved.**

The locked M180/M182, M186/M189, M192/M195, and M248/M249 checksum
inventories all pass. M186's full prefixes are the positive channel-mass
mixture of its conditional J=1 and J=2 prefixes, with J=0 canceled.

The new step is a discrete Hardy--Abel transfer. If
X_D=sum_(2<=d<=D)x_d, then

~~~text
|X_m|/m+sum_(D=2)^(m-1)|X_D|/D^2
 <=3 sum_(d=2)^m |x_d|/d.
~~~

M186/M189's audited J=1 estimates apply this to the exact one-run
coefficient delta_d and two-run convolution coefficient epsilon_d, proving
channel-one WPCR. Conditional on DV, M192/M195 plus accepted M248/M249 DE
prove the conditional J=2 prefix bound and hence channel-two WPCR.
Positivity of the channel masses then proves full WPCR. The explicit
constant is recorded in post_j2_wpcr_theorem.md.

No cross-channel cancellation is needed. PCR does not follow from the
accepted weighted J=1 estimates: it still requires the literal unweighted
J1-PCR lemma, in particular the two-run convolution prefix.

This mission makes no SCBR, BR, PCS, comparison, spectral-gap, mixing-time,
or Terminal inference. Fresh independent audit is required before promotion.

The narrow standard-library checker proof_sanity_check.py verifies the exact
Hardy coefficient bound for 32,637 finite (m,d) rows and the two endpoint
absorptions for 127 odd ranks. This is falsification only; the displayed
all-rank inequalities are the proof.
