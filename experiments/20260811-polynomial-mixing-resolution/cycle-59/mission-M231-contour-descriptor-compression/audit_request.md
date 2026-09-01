# M231 fresh immutable audit request

Treat M231 as immutable. First verify every `SHA256SUMS` payload and the top
digest supplied by the coordinator. Then use a clean-room checker with no
M231/predecessor code import or machine-data read.

Audit only the following claims:

1. both quotients were textually fixed before endpoint generation, with no
   third candidate or post-result tuning;
2. the declared literal word map factors through
   `Z_1=(v,late,ascent,epsilon)` and then through `Z_2`, which is `("closed",)`
   for `late OR ascent` and `("open",v,epsilon)` otherwise;
3. two exact tree constructions give the complete 125-tree template and the
   four odd edits give 500 rows;
4. full `D_B` has `101,101,101,101` classes; `Z_1` has `12,7,6,2` classes
   and 27 globally; `Z_2` has `6,4,3,2` classes and 12 globally;
5. every quotient class is formula-word homogeneous and all 500 endpoint
   replays pass, with no word or behavior collision;
6. the 12 `Z_2` classes match the 12 odd formula words, and adding the two
   fixed boundary words yields 14 full-table words;
7. exact digests are
   `43f9171c42c7b99be6de5b154a34cfc1cee0cee67c1db24743900df2f5d51ad3`
   for rows, `50e4027978e590b6794c608a7d181d6c7bb9171d4f711baf624be6c56e31f2c2`
   for `Z_1`, and
   `fdf2836fee0b96d78a0bcf8c29b06a1a99b5209bcd8ac8e0c069efab34c8c512`
   for `Z_2`;
8. the conclusion is a finite formula/endpoint reduction only, with no
   all-`d`, every-color, total-length, gap, mixing, or Terminal inference.

Return explicit `ACCEPT` or `REJECT` with numbered material/nonmaterial
objections, freeze the referee artifacts and hashes, and stop.
