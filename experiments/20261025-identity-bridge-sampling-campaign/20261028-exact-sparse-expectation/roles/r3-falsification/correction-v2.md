# R3 correction v2 — explicit preparation constant

Coordinator exact read found a local bookkeeping error in falsification-proof-v1.md SectionA. Its hypotheses allowed a separate preparation bound KP^s and a remainder bound KP^s(1+H), but its displayedA3 only chargedKP^s(1+EH). With both terms separately present, the direct sum isKP^s(2+EH). The exact v1 coefficient assertion is rejected; v1 is retained byte-for-byte.

Repaired statement: preparation has expected cost<=K0P^s, and for every full macro the conditional remainder has expected cost<=K1P^s(1+H). Then E total<=P^s[K0+K1(1+EH)]<=(K0+K1)P^s(1+EH), sinceH>=0. When preparation is already included, setK0=0. Both constants are uniform over inputs/macros/precision.

falsification-proof-v2.md makes precisely this correction and marksA3 plus dependent conditional sparse conclusions REPAIRED-PENDING-RECHECK. The finite moment lemma, exact count tests, actual S4m4 product counterexample, finite-degree pointwise bound and EC-OBSTR proof are unchanged. No production code or mathematical experiment changed, so rerunning those finite counts would not test the edited coefficient issue. Fresh exact-version review must inspect this addition and verify that no separate cost is double-counted or lost. A simple boundary checkH=0,K0=K1=1 gives total bound2P^s, exposing v1's coefficientP^s and matching v2. Main mission remains OPEN.
