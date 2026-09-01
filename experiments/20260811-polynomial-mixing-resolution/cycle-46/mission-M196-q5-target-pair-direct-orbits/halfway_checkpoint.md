# M196 search checkpoint

Date: 2026-08-13 UTC.

The immutable M191/M194 manifest gates passed. The frozen 8,400-state action
digest is

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae.
```

The chronological first-coordinate transversal maps the 54 named target rows
to 41 distinct adjusted second IDs. A target-directed bidirectional search has
now completed in 0.5166 seconds, well below the five-minute cap:

```text
forward radius:                  8
complete forward-ball states:   154,393
adjusted targets decided:       41 / 41 positive
original targets decided:       54 / 54 positive
unresolved targets:             0
negative claims:                0
```

Fifteen adjusted targets are direct forward-ball hits. The remaining 26 have
an explicit forward-meeting/reversed-backward certificate. Maximum segment
lengths are forward 8 and backward 7; the longest stabilizer word is 15.
Appending the stored first-coordinate tree word (maximum 9) gives maximum full
endpoint-word length 22.

Every full word is explicitly archived in `targeted_results.json` and has been
replayed on both coordinates by the independent verifier. These word lengths
are exact finite `d=5` certificate facts only, not a polynomial-length claim.
No full stabilizer orbit or `Q_5^2` enumeration was performed.
