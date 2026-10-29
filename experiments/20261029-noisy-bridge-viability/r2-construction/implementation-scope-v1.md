# Implementation scope and exact injection tapes v1

The runnable candidates_v1.py is a small-case standard-library implementation. Its rng.sample(range(N),v) call requires the Python range length to fit Py_ssize_t; the finite checks do not execute enormous schedule values N=lambda^6. This machine restriction is not an asymptotic sampler claim. random.Random supplies fixed reproducibility tapes, not a cryptographic randomness implementation. The mathematical laws in C1-v1 and C2-v1 use exact independent finite uniform choices.

For arbitrary-precision N with v<=N, the same uniform ordered injection law is generated without materializing [N] by this sparse Fisher--Yates pseudocode (zero-based labels):

    D := empty dictionary
    for j=0,...,v-1:
        last := N-j-1
        u := exact_uniform_integer(0,last)
        x := D.get(u,u)
        D[u] := D.get(last,last)
        delete D[last] if present
        emit x

At each stage, D represents the values at the active array addresses 0,...,last; unspecified addresses equal themselves. Selecting a uniform address, returning its value, and replacing it by the last active value deletes a uniform element. Thus every ordered injection has probability 1/(N)_v. If u=last, the subsequent deletion is correct because the last address leaves the active set. Dictionary size is O(v). Uniform_integer uses independent unbiased bits with rejection above the desired range, accepting with probability at least 1/2; expected O(log N) bits and polynomial bit work per emitted label. Each Hurwitz position/sign uses fresh exact finite draws in the same way. No cryptographic PRG assumption is needed or supplied.

This is an implementation of the already frozen distribution, not a third candidate, compiler or law change. It removes the unnecessary materialization of N labels from asymptotic pseudocode. The executable's role remains small-case verification only. Full-word output has L gates, so all claimed costs are measured in N,L,lambda and label bit lengths, never merely log N wires.
