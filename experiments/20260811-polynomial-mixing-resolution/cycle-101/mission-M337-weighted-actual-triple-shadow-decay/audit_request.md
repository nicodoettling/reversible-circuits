# M337 request for fresh immutable audit

Date: 2026-08-14 UTC

Please assign a genuinely fresh referee for frozen M337. The audit should:

1. verify the M337 top digest and every payload;
2. authenticate all fourteen source packages and the actual corrected M296
   digest;
3. independently derive `(1.1)--(1.2)` and Lemma 2.1 of
   `pivot_averaging.md` for arbitrary nonnegative weights;
4. independently derive the whole-child shadow Fubini identity and normalized
   active-pivot average `(3.1)--(3.3)`;
5. check every anchor, exponent, stopping, and terminal-step weight quantifier
   in W-RATSD+HLDT and its conditional telescoping proof;
6. enforce that the `d=3` calculation refutes only a generic averaging route,
   not actual `d>=6` AHTSS/AHLDT;
7. leave HPRN, WRAD, routing, gap, mixing, Terminal, and all downstream gates
   unresolved.

No `d=6` census, induced-child substitution, or replacement candidate is
part of this audit.

