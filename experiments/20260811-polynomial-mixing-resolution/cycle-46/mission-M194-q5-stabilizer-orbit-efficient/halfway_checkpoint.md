# M194 cap checkpoint

Date: 2026-08-13 UTC.

## Immutable gate

M191's complete manifest passed, with top digest

```text
a2aeba9feb5a4bbc3f2161864cfa42ecbc0ef3a578f6a3222c1a9e07c73ab42e.
```

Its frozen action digest was independently recomputed as

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae.
```

All fourteen action rows are bijections and all seven signed pairs are mutual
inverses.

## Exact algorithm and completed stage

The checker built a chronological BFS transversal from first source ID 16 to
all 8,400 quotient points and directly replayed every tree word. Its literal
Schreier generator convention was

```text
s_(x,g)=t_x g t_(xg)^(-1),
```

which fixes ID 16 under the right action. It then streamed these loops on
second source ID 0, retaining orbit-enlarging generators and closing under the
retained generators and inverses.

## Cap outcome

The internal five-minute deadline was reached during exact Schreier-orbit
closure. The script raised `TimeoutError` at 300 seconds and wrote no result
JSON. Observed RSS was approximately 26 MiB, so memory stayed modest; time was
the limiting resource.

The final verdict is therefore **INCONCLUSIVE**. There is no complete orbit,
no 54-target classification, no new route, and no negative obstruction. M188's
fourteen immutable positive routes remain the only accepted memberships.
