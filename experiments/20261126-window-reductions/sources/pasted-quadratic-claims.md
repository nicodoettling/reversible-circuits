# Additional quadratic-length claims supplied by the user

Received in the active conversation, 2026-11-26, in response to the request
for the missing excerpts. This is a transcription of the mathematical
claims and proof obligations, not a verbatim transcript of the entire message.
The user supplied no separate proof document for this addition.

Model: all ordered transposition identity words, rightmost-first products,
half-lazy uniform adjacent-pair same-product heat bath. Set
`m=2 floor(N^2/2)` and `G_j=t_1...t_j`.

1. Any nontrivial cut determined by any tuple of prefixes at times separated
   from each other and from both ends by at least `4N log N+2` has two-sided
   cut ratio at least `c/(mN)`. The midpoint derangement event is balanced
   and attains order `N^-3`.
2. The quotient under simultaneous relabeling, weighted by orbit sizes,
   is claimed to satisfy
   `c min(Phi(quotient),N^-5) <= Phi(P) <= Phi(quotient)`.
   For general even `m=Theta(N^2)`, the supplied claim replaces `N^-5`
   by `N^-7`. The argument selects repeated gates, extracts a front square
   by Hurwitz moves, refreshes the square, transports it through the word,
   and thereby conjugates all gates. Polynomial path congestion is asserted
   but its encoding and constants are not given.
3. The sum of fixed-point counts at N consecutive central prefix times is
   relabeling-invariant, has variance `Omega(N^2)` and Dirichlet form
   `O(1/m)`. Thus even the quotient has gap `O(1/(mN^2))` and mixing lower
   bound `Omega(N^4)`.
4. Superpolynomial mixing at quadratic length remains unresolved. The
   proposed remaining cuts are invariant under relabeling but not determined
   by well-separated prefix observations.

The message cites Diaconis--Shahshahani, *Generating a random permutation
with random transpositions*, at
https://www.imo.universite-paris-saclay.fr/~pierre-loic.meliot/symmetric/texts/Diaconis,%20Shahshahani%20-%20Generating%20a%20random%20permutation%20with%20random%20transpositions.pdf
The source was opened during this audit. Its random-transposition measure
includes identity with probability 1/N; the manuscript instead uses the
explicit nonholding, parity-aware contents-ratio argument of CB.7. No
ordinary endpoint-walk mixing theorem is substituted for bridge dynamics.
