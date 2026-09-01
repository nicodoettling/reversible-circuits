# M45 halfway checkpoint: M43 frozen theorem survives the new-core audit

## Referee status

The new M43 ingredients survive an independent line-by-line check.  Subject
to the explicitly inherited M25/M31/M37/M40/M42 lemmas at their frozen
scopes, the scoped theorem is **ACCEPT**.  No terminal conclusion follows.

## Checks completed

1. **Ordered first-uncovered hulls.**  Every coordinate outside the union of
   update windows remains `H=Stab(z)`-internal.  Each overlap hull retains its
   original `H`-valued ordered product.  After trimming internal factors, the
   globally first remaining crossing begins with inverse-prefix state `z`;
   the trimmed `H` product forces a return.  Factors between ordered hulls are
   internal, so induction restarts from `z`.  Thus hulls contain consecutive
   whole canonical primitive excursions.  An arbitrary hull considered out
   of order would be invalid, but the proof does not do that.

2. **Segmentation arithmetic.**  A component of `u` windows has span at most
   `4u+1`.  With `q(L)=ceil((L-1)/4)` and primitive lengths
   `L_i>=4q_i-2`, joining across gap `g` costs at least `q_1+q_2` for
   `g>=3` and at least `q_1+q_2-1` for `g<=2`.  Hence
   `p=Q-h<=a` exactly as claimed.

3. **One endpoint penalty.**  Once primitive words and all gap lengths are
   fixed, every primitive product belongs to `H`.  The internal
   transposition class sum is central in `C[H]`, so the interspersed gap sums
   combine to one coefficient of `C^G` at one parity-compatible endpoint.
   The report neither assumes independent gap bridges nor pays the endpoint
   factorial repeatedly.

4. **Primitive and renewal coefficients.**  A primitive length-`l` path has
   `d(M-1)^(l-2)` realizations.  For budget `q`, its weight relative to
   `E^l` is `y A^(4(q-1))D_A`.  For `c=k+h,Q=p+h`, the two composition/gap
   binomials multiply to
   `binom(p-1,k-1)(p)^(over h)/h!`.  Summing the extra short returns gives
   `(1-3yD_A)^(-p)`.  Extending infeasible `h` only enlarges the outer upper
   bound, and at `p<=m/10^8,N>=10^12` the factor is below two.

5. **Hard rods.**  With `k-1` long gaps, subtracting three from each and
   distributing the leading/trailing gaps gives
   `binom(m-L-R-2k+3,k)`.  The clean source with four reserved trailing
   factors has exactly `binom(m-L-2k-1,k)` layouts.  The stated primitive
   length bounds give the two tops used in M43.  The fixed-`k` ratio has an
   `exp(-3(a-p)/N)` tail; `k>ceil(20sqrt(a))` is geometric with ratio at most
   `1/5`.

6. **Injectivity and endpoint conditioning.**  In a clean source, inverse
   prefix return times recover the primitive intervals; their lengths recover
   budgets/residues and the remaining positions recover every gap and core
   factor.  M42's bad-core subtraction is uniform in deterministic kicks and
   every compatible endpoint and pays one `d!`; at `a/m<=10^-8` its away
   allowance remains below `2*10^-7`.

7. **Exit and normalization.**  If `h=b_1b_2b_3b_4`, then
   `t h = h(h^-1 t h)`, so the displayed five-word replacement preserves the
   ordered product.  In inverse-prefix coordinates it delays the final return
   by four positions and raises its primitive budget by one.  M42 robustness
   rules out every alternative cut.  The selected outcome has probability at
   least `1/[6(m-4)M^4]`: `1/2` nonlazy mass, `1/3` block-size choice,
   `1/(m-4)` scan, and a fiber of size at most `M^4`; all other
   `Q_3,Q_4,Q_5` terms are nonnegative.

8. **Threshold splice.**  M25 supplies `a=0`, M42 supplies
   `1<=a<=floor(N^2 log log N/100)`, and for `N>=10^12` this overlaps the
   direct M43 range before `floor(m/10^8)`.  Positivity of all binomial tops
   and the no-crossing absorption hold there.  Floors only shrink the range.

## Strongest remaining concern

The acceptance is scoped: conductance need not be monotone in `a`, and the
argument loses its dense robust core at a genuinely large fraction of `m`.
The live red-team question is therefore whether a later-radius literal shell
or a different full-support statistic has balanced stationary mass and
superpolynomial full-`K` boundary suppression.

## Next action

Attack later radii through an exact distance-covering observation first, then
test dense full-support candidates.  Any proposed cut will be discarded
unless its stationary orientation and all three heat-bath boundary terms can
be proved.
