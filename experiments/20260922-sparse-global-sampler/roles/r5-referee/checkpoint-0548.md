# Checkpoint 2026-09-22 05:48 UTC

Status: blind, candidate independent proof in progress (not yet promoted).

Primary sources opened: Dubrovin–Yang–Zagier Classical Hurwitz Numbers, Proposition 1 / equations (13), (17), and the exact connected/disconnected normalization at (19)–(20); Vakil genus 0/1 paper introduction; Chapuy–Louf–Walsh 2206.11315 introduction. The latter covers linear length, not the requested sparse regime. DYZ fixed-genus asymptotics are not uniform in genus.

Promising independent bound: write C_v(x)=sum_g C(v,2v-2+2g)x^(2v-2+2g)/(v!(2v-2+2g)!). The positive quadratic recurrence gives C_v(x) <= [v^(v-3)/v!] x^(2v-2) exp(x v(v-1)/2) for x>=0, by induction, because 2(cosh(kx)-1)/(kx)^2 <= exp(kx). Need verify normalization and check finite cases.

Separate elementary insertion comparison: for b(N,2k)=B(N,2k)/(2k)!, inserting r isolated double-edge components gives b(N,2k-2r)/b(N,2k) <= [4k/(N-2k+1)^2]^r when N>=2k. The output has at most k removable double-edge components, controlling preimage multiplicity by binom(k,r). Need audit factorials and support<=length carefully.

Together these suggest an all-large-component tail, stronger than the proposed g>=2 tail. No current candidate or other worker output read.
