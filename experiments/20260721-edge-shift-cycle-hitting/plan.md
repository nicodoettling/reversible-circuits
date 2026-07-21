# Edge-Shift Hitting Time versus Cycle Structure

## Objective

Estimate the hitting time for creating a parallel edge under the graph
edge-shift process, starting from simple graphs in which every vertex belongs
to at least one simple cycle.  Measure how hitting time relates to:

- edge and vertex counts;
- cycle rank `beta = |E| - |V| + components`;
- number and lengths of distinct simple cycles when exact enumeration is
  feasible;
- lengths in a deterministic fundamental cycle basis when exact simple-cycle
  enumeration is too expensive;
- topology: disjoint cycles, cycles sharing one vertex, theta graphs, and a
  Hamiltonian cycle with random chords.

This is a graph-only experiment.  It does not model the ordering constraint of
a transposition circuit word.

## Process Definition

Before absorption the state is a finite simple undirected graph `G=(V,E)`.
One step is:

1. Choose uniformly an ordered wedge `(a,b,c)` with `a != c` and
   `{a,b},{b,c} in E`.
2. If `{a,c} in E`, stop and record a hit.  Replacing `{a,b}` by another copy
   of `{a,c}` would create two parallel edges between `a` and `c`.
3. Otherwise set

   ```text
   E <- E - {{a,b}} + {{a,c}}.
   ```

The vertex set, number of edges, connected-component partition, and cycle
rank are invariant before the hit.  The requirement that every vertex lies on
a cycle is imposed only at time zero and is not preserved by the move.

## Meaning of “Number of Cycles”

The experiment keeps two different quantities separate:

1. **Cycle rank** is scalable, canonical, and invariant, but counts independent
   binary cycles rather than distinct simple cycles.
2. **Distinct simple-cycle count and length histogram** answer the literal
   cycle-count question, but can be exponentially large.  They are computed
   exactly by enumerating the binary cycle space only when the cycle rank is at
   most the configured cap.

The fundamental-cycle-basis lengths are always recorded as a scalable proxy;
they depend on the deterministic spanning forest and are not claimed to be a
minimum cycle basis.

## Ensembles

- `disjoint_cycles`: exactly the listed disjoint cycles.
- `cycle_bouquet`: listed cycles share one center vertex and no edges; there
  are exactly as many simple cycles as listed.
- `theta`: three internally disjoint paths between two endpoints; cycle rank
  two and exactly three simple cycles.
- `cycle_with_chords`: a random Hamiltonian cycle plus `beta-1` random chords;
  this permits extensively overlapping cycles while keeping every vertex on
  the Hamiltonian cycle.
- `edge_list`: an explicit graph supplied directly in a configuration.

## Output and Analysis

Raw output is JSON Lines with:

- one `graph_summary` record per generated graph;
- one `walk_trial` record per Monte Carlo trajectory;
- one `graph_complete` checkpoint used by `--resume`.

Censored trials report `observed_steps=max_steps`.  The analysis reports both
the conditional mean among hits and the restricted mean
`E[min(tau,max_steps)]`; it never silently treats the conditional mean as the
unconditional hitting time.

The analysis script creates graph- and setting-level CSV files and two
exploratory log-linear fits.  These fits are empirical scaling diagnostics,
not mixing-time or hitting-time proofs.
