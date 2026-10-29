"""C1-v1/C2-v1 exact algorithms. Standard library; rightmost-first products.
Random.Random is only a reproducible finite-test tape, not a cryptographic RNG.
The mathematical sampler uses independent exact uniform finite draws.
"""
from itertools import combinations


def edge(a, b):
    if a == b:
        raise ValueError("a transposition needs distinct endpoints")
    return (a, b) if a < b else (b, a)


def evaluate(n, word):
    p = list(range(n))
    for a, b in word:
        if not (0 <= a < b < n):
            raise ValueError("invalid canonical edge")
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def conjugate(u, by):
    a, b = by
    def act(x):
        return b if x == a else a if x == b else x
    return edge(act(u[0]), act(u[1]))


def hurwitz_at(word, i, inverse=False):
    result = list(word)
    u, v = result[i:i+2]
    result[i:i+2] = (conjugate(v, u), u) if inverse else (v, conjugate(u, v))
    return result


def scramble(word, steps, rng):
    if steps < 0:
        raise ValueError("negative step count")
    out = list(word)
    if steps and len(out) < 2:
        raise ValueError("no adjacent pair")
    for _ in range(steps):
        i = rng.randrange(len(out)-1)
        u, v = out[i], out[i+1]
        if rng.randrange(2):
            out[i], out[i+1] = conjugate(v, u), u
        else:
            out[i], out[i+1] = v, conjugate(u, v)
    return out


def c1_block(labels):
    a, b, c, d = labels
    if len(set(labels)) != 4:
        raise ValueError("C1 requires four distinct labels")
    return [edge(a,c), edge(c,d), edge(a,b), edge(a,d), edge(b,c), edge(b,d)]


def c1(n, blocks, steps, rng):
    if n < 4 or blocks < 1:
        raise ValueError("C1 requires N>=4 and B>=1")
    word = []
    for _ in range(blocks):
        word.extend(c1_block(rng.sample(range(n),4)))
    return scramble(word, steps, rng)


def c2_word(labels):
    if len(labels) < 3 or len(set(labels)) != len(labels):
        raise ValueError("C2 needs an injection of at least three labels")
    return ([edge(a,b) for a,b in zip(labels,labels[1:])]
            + [edge(labels[0],b) for b in labels[1:]])


def c2(n, m, steps, rng):
    if m < 2 or n < m+1:
        raise ValueError("C2 requires m>=2 and N>=m+1")
    return scramble(c2_word(rng.sample(range(n),m+1)),steps,rng)


def replacement(n, word, k, rng):
    if n < 2 or not (0 <= k <= len(word)):
        raise ValueError("invalid M0 parameters")
    out = list(word)
    for i in rng.sample(range(len(out)),k):
        a = rng.randrange(n)
        b = rng.randrange(n-1)
        if b >= a:
            b += 1
        out[i] = edge(a,b)
    return out


def support(word):
    return set(x for e in word for x in e)


def null_six_count(n, word):
    if len(word) % 6:
        raise ValueError("requires aligned six-gate blocks")
    identity = tuple(range(n))
    return sum(evaluate(n,word[i:i+6]) == identity for i in range(0,len(word),6))
