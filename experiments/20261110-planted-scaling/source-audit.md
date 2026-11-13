# Scoped literature dependency check

Read 2026-11-10. Obligation: control the relative pointwise completion error
for the pure-transposition walk at length N^2-O(N), including its period two.
No broad hardness or planted-problem literature review was performed.

Primary source: Persi Diaconis and Mehrdad Shahshahani, *Generating a Random
Permutation with Random Transpositions*, Z. Wahrscheinlichkeitstheorie verw.
Gebiete 57 (1981), 159–179.
[Author-paper PDF](https://www.imo.universite-paris-saclay.fr/~pierre-loic.meliot/symmetric/texts/Diaconis,%20Shahshahani%20-%20Generating%20a%20random%20permutation%20with%20random%20transpositions.pdf).

Checked passages: measure (1.1), Theorem 1 and its scaling (1.4); inversion
formula (2.2); Lemmas 6–8 (tableaux, transposition character ratio and conjugate
partitions); Lemma 14 and its Plancherel identity (3.1), printed p168;
the end of section 3, printed pp173–174, which bounds that Fourier sum, not
merely total variation. The source's variation norm is twice our TV; no
attack advantage is inferred by confusing those normalizations.

Cross-check of the explicit L2 statement: Laurent Saloff-Coste,
*Random Walks on Finite Groups*, Theorem 9.2, printed p327,
[author-hosted PDF](https://pi.math.cornell.edu/~lsc/papers/chap5.pdf).
For the source walk, d2 at t=(N/2)(log N+c) is at most A exp(-c), with an
absolute A. This is the same bound supplied by the primary paper's Fourier
sum. The finite calculations use the exact spectrum and require no value of A.

## Hypotheses and convention translation

The source chooses two labels independently, so identity has mass 1/N and
each transposition mass 2/N^2. Our generator law assigns zero identity mass
and weight 1/q to each transposition. The eigenvalues are related by
alpha_lambda=1/N+(N-1)theta_lambda/N. Conjugate partitions have equal dimension
and opposite pure-transposition character ratio (primary Lemma 8).

Pair those ratios, omit the trivial and sign modes from the pure walk, and
compare the even-power sum with the source L2 sum. This gives the bound in
proof.md section 5; odd lengths follow by contraction between parity classes.
The target is uniform on the appropriate parity class, not uniform on all S_N.
Only the relative completion bound is imported. No claim about exact bridge
sampling or local bridge-chain mixing follows from this source.

For exact finite counts, let c_lambda be the sum of diagram contents and
d_lambda the number of standard tableaux, computed by removing the largest
entry at a corner. The character formula and inversion yield
Z_j=(1/N!) sum_lambda d_lambda^2 c_lambda^j. For even j,
delta_j=(N! Z_j)/(2 q^j)-1. The checker verifies these counts by an independently
implemented elementary cut/join recurrence at N2..8. Products versus inverse
products do not alter this identity-return count; transpositions are their
own inverses. The experiment consistently evaluates products rightmost first.

Status: **source statement and convention translation checked**. This is a
scoped dependency audit, not an independent review of the new attack proof.
