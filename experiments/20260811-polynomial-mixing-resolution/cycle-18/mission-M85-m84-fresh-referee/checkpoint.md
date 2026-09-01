# M85 halfway checkpoint

Date: 2026-08-12.

The assigned frozen digests match exactly:

```text
report.md             c55f51c6ff05d7af7e79b3679a707fcf252112dfe6c3e7de4ef6213a501f8b12
zero_row_theorem.md   78130a18f581c9d6a2fdcb6ed2c854287fba43dd9128d5dc2405b9771598364e
SHA256SUMS            7107346acc1a140177f51052e2eb2d25af6204d4622ca1aab074d16e43275372
```

All eighteen entries in M84's `SHA256SUMS` verify.  The subset formula,
outside-strand transparency, dual cut criterion, torus-cover subgroup, and
matching-block coordinate count have been reconstructed on paper.  No
material objection has appeared so far.

The most delicate point is correctly distinguishing the two types of local
slides.  When an unselected interval factor is crossed by the selected pair
strand, that interval factor is slid and the pair annulus is unchanged.  When
an already selected between-factor crosses the still-residual left pair
strand, the pair strand is slid along that factor; these are exactly the two
token tracks in the collision contour.  This resolves the apparent risk that
unselected interval factors were omitted from the contour.

The independent exact checker is being used only to attack these interfaces;
it will not substitute finite evidence for the all-modulus proof.
