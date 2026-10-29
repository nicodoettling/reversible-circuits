# Checker v1 rejection before execution

The source-only review caught count_d computing factorial(N)/factorial(N-2m), which is mathematically correct but computationally impossible at N=lambda^6. Version 1 was never executed and must not be run. Version 2 replaces that quotient by the explicit 2m-factor falling product, and retains exact arithmetic. This is an implementation/resource-planning failure, not a counterexample to D(N,m). No bounded job failed; no raw result was produced. The older source remains immutable evidence.
