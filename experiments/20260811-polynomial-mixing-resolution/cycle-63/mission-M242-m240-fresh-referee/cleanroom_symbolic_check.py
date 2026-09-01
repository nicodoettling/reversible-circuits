#!/usr/bin/env python3
"""Clean-room M242 checks of the algebra after IDL.

No M240 module or data is imported or read. Synthetic IDL words are built
directly from the lemma's displayed coordinates. These checks audit the proof
algebra; they do not prove IDL.
"""
from __future__ import annotations
import hashlib
import itertools
import json
import platform
from pathlib import Path

OUTPUT = Path(__file__).with_name("cleanroom_results.json")

def edge(a, b):
    assert a != b
    return (a, b) if a < b else (b, a)

def conj(t, by):
    a, b = by
    def image(x):
        return b if x == a else a if x == b else x
    return edge(image(t[0]), image(t[1]))

def move(word, signed):
    j = abs(signed) - 1
    a, b = word[j:j+2]
    out = list(word)
    if signed > 0:
        out[j:j+2] = (b, conj(a, b))
    else:
        out[j:j+2] = (conj(b, a), a)
    return tuple(out)

def act(word, route):
    for signed in route:
        word = move(word, signed)
    return word

def inverse(route):
    return tuple(-signed for signed in reversed(route))

def sign_automaton(bits):
    if not bits:
        return ()
    signs = [-1 if bits[0] else 1]
    for bit in bits[1:]:
        signs.append(-1 if bit else -signs[-1])
    return tuple(signs)

def synthetic_idl(d, v, bits):
    x, y, z, n = v-1, d-1, 0, d
    size = 2*d
    source = [edge(d+1+2*j, d+2+2*j) for j in range(size)]
    target = list(source)
    source[2*v-3] = edge(x, y)
    target[2*v-3] = edge(x, n)
    for t, child in enumerate(bits):
        r, u = v+t+1, v+t
        a, b = 2*r-4, 2*r-3
        if child:
            source[a] = source[b] = edge(u, y)
            target[a] = target[b] = edge(u, n)
        else:
            h = edge(z, d+1+2*r)
            source[a] = source[b] = h
            target[a] = target[b] = h
    source[2*d-4:2*d] = (edge(z,x), edge(z,y), edge(z,n), edge(z,n))
    target[2*d-4:2*d] = (edge(z,y), edge(z,y), edge(z,x), edge(z,n))
    return tuple(source), tuple(target)

def route(d, v, bits):
    signs = sign_automaton(bits)
    q = tuple(s for t,e in enumerate(signs)
              for s in (e*(2*(v+t)-2), e*(2*(v+t)-1)))
    b = (-(2*d-4), 2*d-3, -(2*d-2), -(2*d-3), -(2*d-4))
    return q, q+b+inverse(q)

def main():
    pos = neg = disjoint = child = carrier = 0
    labels = range(7)
    trans = tuple(edge(a,b) for a in labels for b in labels if a < b)
    for c in trans:
        for h in trans:
            assert act((c,h,h),(1,2)) == (h,h,c)
            chc = conj(h,c)
            assert act((c,h,h),(-1,-2)) == (chc,chc,c)
            pos += 1; neg += 1
    for x,y,n,u,a,b in itertools.permutations(labels,6):
        if set((a,b)).isdisjoint((x,y,n)):
            h = edge(a,b)
            for c in (edge(x,y),edge(x,n)):
                assert act((c,h,h),(1,2)) == (h,h,c)
                assert act((c,h,h),(-1,-2)) == (h,h,c)
                disjoint += 1
        cy,hy,cn,hn = edge(x,y),edge(u,y),edge(x,n),edge(u,n)
        common = edge(u,x)
        assert act((cy,hy,hy),(-1,-2)) == (common,common,cy)
        assert act((cn,hn,hn),(-1,-2)) == (common,common,cn)
        child += 1
    for x,y,z,n in itertools.permutations(labels,4):
        source=(edge(x,y),edge(z,x),edge(z,y),edge(z,n))
        target=(edge(x,n),edge(z,y),edge(z,y),edge(z,x))
        assert act(source,(-1,2,-3,-2,-1)) == target
        carrier += 1
    synthetic = 0
    for d in range(5,12):
        for v in range(2,d):
            L=d-v-1
            for bits in itertools.product((0,1),repeat=L):
                source,target=synthetic_idl(d,v,bits)
                q,full=route(d,v,bits)
                assert act(source,full)==target
                assert act(target,q+inverse(q))==target
                assert len(full)==4*L+5
                assert all(not bit or sign==-1 for bit,sign in zip(bits,sign_automaton(bits)))
                synthetic += 1
    overlap=0
    for x,y,z in itertools.permutations(labels,3):
        a,b=edge(x,y),edge(z,x)
        assert act((a,b,a),(-1,-1))==(b,conj(b,a),a)
        overlap += 1
    a,b=edge(0,1),edge(2,3)
    actual=act((a,b,a),(-1,-1)); claimed=(b,conj(b,a),a)
    assert actual != claimed
    checks={"positive_square":pos,"negative_square":neg,
            "disjoint_square_both_signs":disjoint,
            "direct_child_equalization":child,"terminal_carrier":carrier,
            "synthetic_idl_routes":synthetic,"length_and_epsilon_checks":synthetic,
            "valid_overlap_fixed_boundary":overlap,
            "generic_fixed_boundary_counterexample":{"a":a,"b":b,
                "actual":actual,"claimed":claimed}}
    normalized=json.dumps(checks,sort_keys=True,separators=(",",":"))
    result={"experiment":"M242 clean-room audit of M240 algebra after IDL",
            "scope":"Synthetic IDL words only; no DPS endpoints; IDL remains unresolved.",
            "all_expected_checks_pass":True,"checks":checks,
            "normalized_digest":hashlib.sha256(normalized.encode()).hexdigest(),
            "environment":{"python":platform.python_version(),"dependencies":{},"seed":None}}
    OUTPUT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
