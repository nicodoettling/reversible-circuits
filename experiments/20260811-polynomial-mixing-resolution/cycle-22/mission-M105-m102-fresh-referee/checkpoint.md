# M105 halfway checkpoint: singular face accepted, topology scope correction required

Date: 2026-08-12. Controlling status: fresh referee audit in progress.

## Frozen provenance

The assigned M102 hashes match exactly:

```text
report.md                    0e8f82a63c0e936e0f466bf9d33f9e1182f58fd48c2491998f0f7f5ffb7a5c1e
bulk_defect_obstruction.md   57c38e10a519ff9f2bdeaf6d0893e18554911337adee9c4001bf13442d8edf4b
SHA256SUMS                   54ac293104a246f087c8ce8571c800301655e01d641769437f43b6398a0257ef
```

`sha256sum -c SHA256SUMS` returned `OK` for all ten frozen M102 entries.  The M94 and M100 manifests also validate completely.

## Independent exact collision reconstruction

`independent_collision_audit.py` imports no predecessor code and derives residual cycles from affine labeled support positions.  It reproduces all five M102 face lists and bases exactly:

```text
source A  2700/29        source B  5400/59
intermediate 89/8100
joint SS 284497920/99373
joint SN 1317120000/398453
```

Thus the two-target-color stripped coefficient is `-8990.626343656686`, with exact negative sign from `5400/59 < 2700/29`.  The nested-intermediate color has no `delta`-zero residual and is bounded on this face.  Restoring `a(s)a(t)=4`, the critical-Borel factor `(2*pi)^-2`, and `n=3k` gives normalized local `k^2 Delta` position-density coefficient

```text
-8990.626343656686 / (9*pi^2) = -101.21565586947543.
```

The radical displayed by M102 is therefore correct as the stripped `J`-integrand coefficient.  It is not by itself the fully normalized coefficient; this is a presentation clarification, not a sign defect.

The explicit affine lists make the remainder rigorous: after extracting the unique `delta^-3/2`, every remaining factor is smooth and bounded away from zero, hence the coefficient function is `G(0)+O(delta)`.  Therefore the remainder is `O(delta^-1/2)`.  The strict negative sign persists uniformly on a small product neighborhood, so the direct support-position integral diverges to `-infinity` there.

## Required scope correction

The frozen proof establishes that exact small-`r` Borel layers are necessary in any matched asymptotic.  It does **not** establish that the named collision/triangle topology is the exact complete matching counterterm, nor that triangle terms specifically cancel the displayed divergence.  Such a claim requires an exhaustive local cell-gluing classification and literal lift/orbit multiplicity identity.  Finiteness of the discrete sum at each `k` does not supply that identity.

Safe wording: discrete small-component layers are mandatory; collision/triangle strata are a candidate same-order boundary/counterterm class that must be included and audited, not a proved complete renormalizer.

## Fresh finite check

`independent_finite_probe.py` imports no M102 or predecessor code.  It reconstructs ordered-pair multiplicities, exact integer completion counts, quotient rows, and the central event; only final matrix arithmetic is floating.  It reproduces:

| `k` | `k*pi(E)` | `k^2 Delta(E)` | negative event orbits | range of `k z` |
|---:|---:|---:|---:|---:|
| 7 | .07314864161123523 | .04320590873435413 | 3/28 | `[-.276094,1.218981]` |
| 9 | .07224023359526269 | .04216566592865655 | 7/60 | `[-.410159,1.350249]` |

The exact event-mass composition formula and event-orbit formula also pass.  The `k=9` minimum is independently the separated-color gaps `(5,5,5,12)` witness.  These are finite checks only.

## Controlling scope

`(MBF)`, existence or nonvanishing of `C_*`, `(BD)`, `(BA2)`, direct signed `L1`, H0, every bridge/identity-chain gap, and both Terminals remain unresolved.  The likely verdict is `ACCEPT` for the singular-face obstruction with one required scope correction to the matching-topology language.
