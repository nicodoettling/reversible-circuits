# M197 substantive checkpoint

Date: 2026-08-13 UTC.
Status: independent normalization and universal aggregate reproduced; final
referee report and freeze pending.

## Integrity gate

- Frozen M193 passes all eight recorded payload hashes. Its exact nine-file
  inventory matches the manifest; `SHA256SUMS` digest is
  `aff1302508bfc61727e47649f0810183ff7fc7f28e7840bc3bbc239e828af0b2`.
- Every checksum in all eighteen cited dependency ledgers passes. No
  predecessor was edited.
- Nonmaterial hygiene caveat: older immutable M117, M162, and M165 currently
  contain unledgered `__pycache__` directories. Their recorded payloads still
  hash correctly. M197 did not remove or modify them.

## Independent audit status

- Re-derived `L_a dmu_parent=pi_a dmu_a` with `pi_a=1/(d+1)` and
  `(eta/pi_a)E[L_a^2||Phi||^2]=eta E_child[L_a||Phi||^2]`. Hence `eta` is
  outside the branch sum while `pi_a` is internal to `G`; killed `a=d`
  leaves exactly `d` branches `a=0,...,d-1` and no survival factor.
- The clean-room symbolic checker starts from M185/M190's raw reset,
  height-one, and unary history expressions. It independently sums
  `D=a+1=1,...,d` and exactly reproduces M193's closed average.
- For `B>=2`, it regenerates the positive `b` derivative, strict concavity
  in `q`,
  `q*=y(d^2+11d+22)/[(d+2)(d+3)(4y+3)]`, the seven positive `y`-derivative
  coefficient rows, and shifted slack coefficients
  `5726736,18788964,16784028,6721029,1351327,131535,4829`.
- The separate `B=1` substitution regenerates M193's nominal average and
  positive slack numerator
  `51529d^4+779710d^3+4228095d^2+9411050d+7219256`. Accepted M179/M184
  activity accounting confirms that deleting inactive rank-one targets can
  only lower this nonnegative nominal envelope.
- The pointwise obstruction survives exactly:
  `Sbar_(3,20,19)=10249528643/7684875000>1`, while the independently summed
  degree average is `443845801/614790000<1`. The proof is genuinely
  observation-averaged.
- Direct exterior sums including `r=n` reproduce
  `sum_r(r+1)eta=(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2)<=36/125`.
  Thus `sum_a B_(d,a)<3d/4` gives exactly `27/125`, with no missing count.
- At `n=0`, the checker independently diagonalizes the exact `d=1` matrix,
  recovers `rho_1=(25+sqrt(415))/70`, `eta=9/16`, and the one-history bound;
  hence the charge is `<9(25+sqrt(415))/1120<3/8`.

Current mathematical disposition: **ACCEPT**, subject only to final write-up
and the nonmaterial predecessor-cache hygiene note. Scope remains `h=3` only.
