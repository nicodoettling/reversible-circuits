# Targeted check reservation request

Claim: actual production getrandbits branches implement exact rejection and categorical ticket selection; LinearMemo replacement preserves one key; explicit DFS expands each (remaining, quotient) at most once; two selected nontrivial components never retain simultaneous counters.

Frozen code: exact_sampler-v1.py SHA25693d38c75d25446dc7287cd65ea0ec4f05c5f3855fe96b3ee26fe6a9444bb33a0. New script targeted-check-v1.py; output targeted-results-v1.json in this owned directory. No script execution before coordinator reservation.

Ranges: integer bounds1..65, every accepted ticket preceded by every possible rejected candidate once; six categorical vectors with zeros, invalid boundaries; exact geometric laws through8 trials with unexecuted tail explicitly calculated, not discarded. Memo/DFS states v2..6, genus0..2; selected repeated v2 components at N5,m4 with interleaving and isolate. Seed1729 only for validity draws; all structural/ticket checks deterministic. Historical full quotient-state checks are not rerun.

Estimate: at most (15)*15*3^5 coarse memo keys across separately discarded instances; actual expected far smaller. Less than128MiB memory, under10s expected; request60s wall and1GiB address-space cap. Detailed JSON atomically published; stdout one short summary below1KiB. No other job may overlap. Coordinator must supply reservation with current helper/run argv; do not manually retranscribe it.
