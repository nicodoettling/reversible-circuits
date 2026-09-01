# M314 sole independent k=11 reconstruction audit

Date: 2026-08-14 UTC

Exactly one independent deterministic reconstruction was run:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-92/mission-M314-m311-fresh-referee/independent_k11_reconstruction.py --output experiments/20260811-polynomial-mixing-resolution/cycle-92/mission-M314-m311-fresh-referee/independent_k11_results.json
```

The standard-library checker fixes `k=11` in source and reads no project or
predecessor code/data.  It constructs the staircase from sorted mass
endpoints rather than M311's cell-dictionary ordering, retains all 11 phases,
and tests only the frozen maximal sign blocks.  There was no frozen-script
replay, second rank, alternate grouping, or replacement search.

The reconstruction exactly matches M311:

- Abel signs `----+++++0` on rungs `1,...,10`;
- 19 transport cells in blocks `[1,4]`, `[5,9]`, `[10,10]` of sizes
  `8,10,1`;
- first lexicographic failure `(u,ell,block)=(1,2,1)`, positive-sign rungs
  `5,...,9`, with value

```text
-2061577314459922172641215612586209282269020583869992685957021396704823223246367368524303337392898219047370249489990505551190598969997087218733977014686080513732765909680273626243354879974696670860872661297162706082605379671283262275186077612570547848875709
/57279694330006960277221458518965386699701247536817041392297378955423047072191462802544866890587366849437209220150089143598727486477148871354092375414658109189979205585843112644773807166449670610550843123177619456000000000000000000000000000000000000000000000
```

  (approximately `-0.03599141613051397`), with the same ten cells and exact
  cell contributions;
- exactly 154 negative blocks among 450, in 118 of 150 rows;
- exactly 150 positive, zero zero, and zero negative complete aggregates;
- exact minimum

```text
34291732207526064450688388422495555455454703972588848856958199485995299466413819734342879740743731574975037081759345906804554572001967138611767316530764100688488400362860310344249859798969692348573873463825659652232073581175965481520538854493399962042973492753252383460336197217321530232668416071
/344335858201293417094522730388183010768667527748907527161408251372132959990255316571142691761578672227274104401373903758062596584539034471242425792814808770445986093838442387010681753974871912514739898241981723035393527061315462735062490405193115324383232000000000000000000000000000000000000000000
```

  (approximately `0.09958803705967692`) at `(2,10)` and `(2,23)`;
- all 75 reflected lag pairs agree exactly for every `Xbar`, `Ybar`, block,
  and aggregate.

The raw JSON stores the complete exact 150-row aggregate and 450-block table.
Exact assertions also verify row/column marginals, QTI, QBD, support coverage,
rung orientation, and reflection.  These are finite facts at `k=11` only.
