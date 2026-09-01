#!/usr/bin/env python3
"""Clean-room exact referee check for frozen M152.

This standard-library-only script imports no predecessor code or data.  It
uses literal compositions rather than M152's grouped-root implementation and
checks only the theorem witness plus a few algebraic audit states.
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import math
import platform
from fractions import Fraction as Q
from pathlib import Path


Poly = tuple[Q, ...]
ROOT = Path(__file__).resolve().parents[4]
M152 = ROOT / "experiments/20260811-polynomial-mixing-resolution/cycle-35/mission-M152-deficit-martingale-potential"

EXPECTED_HASHES = {
    "report.md": "f1dafebd7f6722a16abedbf5382ad433e729f5294295f06b23fb6d82eb97bd70",
    "beta_jensen_obstruction.md": "dfebb6c250f6c4fcf0eaf44da961d0887613ad28012689b52b6a40c441023b6d",
    "beta_potential.py": "5c9cd1a4693859147d0f356f30e997e2d3e8c1c04f6ead4c8d4ff4740edf4388",
    "beta_potential.json": "b4880001fb4b8b706c40ee58ca14dd90649efc204dbdf2a31c551c0c597eb6fa",
    "freeze_manifest.md": "0c444c254bd49c008cd4836f14d16ecc43aa8aace628e5177278e2457304db51",
    "SHA256SUMS": "141a6d131e4d1c36e6d5d2716d249ee157544084269e28ac78c279ba02fc94c6",
}


def clean(a: list[Q] | tuple[Q, ...]) -> Poly:
    out = list(a)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def padd(a: Poly, b: Poly) -> Poly:
    out = [Q(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return clean(out)


def pscale(c: Q, a: Poly) -> Poly:
    return clean([c * value for value in a])


def pmul(a: Poly, b: Poly) -> Poly:
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return clean(out)


def mono(degree: int, coefficient: Q = Q(1)) -> Poly:
    return tuple([Q(0)] * degree + [coefficient])


def one_minus_u(degree: int) -> Poly:
    return padd((Q(1),), mono(degree, Q(-1)))


def rising(a: int, n: int) -> int:
    return math.prod(range(a, a + n))


def beta_mean(poly: Poly, kappa: int, deficit: int) -> Q:
    return sum(
        (
            coefficient * Q(rising(deficit, degree), rising(kappa, degree))
            for degree, coefficient in enumerate(poly)
        ),
        Q(0),
    )


@functools.lru_cache(None)
def w(n: int) -> Q:
    return Q(n ** (n - 1), math.factorial(n))


def qsplit(s: int, bottom: int) -> Q:
    return w(s + 1 - bottom) * w(bottom) / w(s + 1)


@functools.lru_cache(None)
def compositions(total: int) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    return tuple(
        (head,) + tail
        for head in range(1, total + 1)
        for tail in compositions(total - head)
    )


def rho(word: tuple[int, ...]) -> Q:
    return Q(math.prod(w(part) for part in word), math.factorial(len(word)) * w(sum(word) + 1))


@functools.lru_cache(None)
def basins(s: int) -> tuple[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...]:
    sources = compositions(s)
    endpoints: set[tuple[int, ...]] = set()
    for source in sources:
        for cut in range(1, len(source)):
            endpoint = (sum(source[:cut]),) + source[cut:]
            if endpoint[0] + endpoint[1] - 1 >= 2:
                endpoints.add(endpoint)
    rows = []
    for endpoint in sorted(endpoints, key=lambda row: (len(row), row)):
        basin = []
        for source in sources:
            for cut in range(1, len(source)):
                if (sum(source[:cut]),) + source[cut:] == endpoint:
                    basin.append(source)
                    break
        rows.append((endpoint, tuple(basin)))
    return tuple(rows)


def point_context(source: tuple[int, ...], bottom: int) -> Poly:
    degree, last = len(source), source[-1]
    if last < bottom:
        return (Q(0),)
    if last == bottom:
        return mono(degree - 1, Q(degree))
    return pscale(qsplit(last - 1, bottom), one_minus_u(degree))


def numeric_context(source: tuple[int, ...], kappa: int, deficit: int, bottom: int) -> Q:
    degree, last = len(source), source[-1]
    if last < bottom:
        return Q(0)
    if last == bottom:
        return Q(degree * rising(deficit, degree - 1), rising(kappa, degree - 1))
    return qsplit(last - 1, bottom) * (
        1 - Q(rising(deficit, degree), rising(kappa, degree))
    )


@functools.lru_cache(None)
def point_reward(s: int, bottom: int) -> Poly:
    q = qsplit(s, bottom)
    answer: Poly = (Q(0),)
    for endpoint, basin in basins(s):
        current: Poly = (Q(0),)
        for source in basin:
            current = padd(
                current,
                pscale(rho(source), padd(point_context(source, bottom), (Q(-q),))),
            )
        capacity = Q(len(endpoint)) * rho(endpoint)
        answer = padd(answer, pscale(Q(1) / (q * capacity), pmul(current, current)))
    return answer


@functools.lru_cache(None)
def exact_reset(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    q = qsplit(s, bottom)
    answer = Q(0)
    for endpoint, basin in basins(s):
        current = sum(
            (
                rho(source)
                * (numeric_context(source, kappa, deficit, bottom) - q)
                for source in basin
            ),
            Q(0),
        )
        answer += current * current / (Q(len(endpoint)) * rho(endpoint))
    return answer


def attachment(kappa: int, deficit: int, degree: int, x: int) -> Q:
    return (
        Q(math.comb(degree, x))
        * rising(deficit, x)
        * rising(kappa - deficit, degree - x)
        / rising(kappa, degree)
    )


@functools.lru_cache(None)
def bellman(bottom: int, excess: int) -> Poly:
    """Minimal pointwise integrand, rebuilt by literal-root enumeration."""
    s, q = bottom + excess, qsplit(bottom + excess, bottom)
    answer = point_reward(s, bottom)
    for source in compositions(s):
        degree, last = len(source), source[-1]
        if last <= bottom or last - 1 < 2:
            continue
        child = bellman(bottom, last - 1 - bottom)
        coefficient = rho(source) * qsplit(last - 1, bottom) / q
        answer = padd(answer, pscale(coefficient, pmul(one_minus_u(degree), child)))
    return answer


@functools.lru_cache(None)
def true_h(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    """Exact unnormalized nilpotent excursion, using literal roots."""
    answer = exact_reset(s, kappa, deficit, bottom)
    for source in compositions(s):
        degree, last = len(source), source[-1]
        if last <= bottom or last - 1 < 2:
            continue
        for x in range(degree):
            answer += (
                rho(source)
                * attachment(kappa, deficit, degree, x)
                * true_h(last - 1, kappa + degree, deficit + x, bottom)
            )
    return answer


@functools.lru_cache(None)
def discrete_majorant(s: int, kappa: int, deficit: int, bottom: int) -> Q:
    q = qsplit(s, bottom)
    answer = beta_mean(point_reward(s, bottom), kappa, deficit)
    for source in compositions(s):
        degree, last = len(source), source[-1]
        if last <= bottom or last - 1 < 2:
            continue
        coefficient = rho(source) * qsplit(last - 1, bottom) / q
        for x in range(degree):
            answer += (
                coefficient
                * attachment(kappa, deficit, degree, x)
                * discrete_majorant(last - 1, kappa + degree, deficit + x, bottom)
            )
    return answer


def record(value: Q) -> dict[str, str | float]:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal": float(value),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    failures: list[str] = []

    observed_hashes = {}
    for name, expected in EXPECTED_HASHES.items():
        observed = hashlib.sha256((M152 / name).read_bytes()).hexdigest()
        observed_hashes[name] = observed
        if observed != expected:
            failures.append(f"immutable hash mismatch: {name}")

    doob_checks = 0
    for kappa, deficit, degree in ((2, 1, 1), (5, 2, 3), (11, 7, 6)):
        for power in range(7):
            psi = mono(power)
            full = sum(
                (
                    attachment(kappa, deficit, degree, x)
                    * beta_mean(psi, kappa + degree, deficit + x)
                    for x in range(degree + 1)
                ),
                Q(0),
            )
            retained = sum(
                (
                    attachment(kappa, deficit, degree, x)
                    * beta_mean(psi, kappa + degree, deficit + x)
                    for x in range(degree)
                ),
                Q(0),
            )
            killed = attachment(kappa, deficit, degree, degree) * beta_mean(
                psi, kappa + degree, deficit + degree
            )
            parent = beta_mean(psi, kappa, deficit)
            rhs_retained = beta_mean(pmul(one_minus_u(degree), psi), kappa, deficit)
            rhs_killed = beta_mean(mono(degree + power), kappa, deficit)
            if full != parent or retained != rhs_retained or killed != rhs_killed:
                failures.append(f"Doob identity failed at {(kappa, deficit, degree, power)}")
            doob_checks += 1

    context_checks = 0
    for s, kappa, deficit, bottom in ((9, 2, 1, 3), (5, 7, 3, 2), (4, 11, 7, 1)):
        for source in compositions(s):
            lifted = beta_mean(point_context(source, bottom), kappa, deficit)
            direct = numeric_context(source, kappa, deficit, bottom)
            if lifted != direct:
                failures.append(f"context identity failed at {(s, kappa, deficit, bottom, source)}")
            context_checks += 1

    bottom, excess, kappa, deficit = 3, 6, 2, 1
    s = bottom + excess
    q = qsplit(s, bottom)
    budget = 1 - q
    poly = bellman(bottom, excess)
    value = beta_mean(poly, kappa, deficit)
    discrete = discrete_majorant(s, kappa, deficit, bottom)
    lifted_reset = beta_mean(point_reward(s, bottom), kappa, deficit)
    reset_over_q = exact_reset(s, kappa, deficit, bottom) / q
    h_over_q = true_h(s, kappa, deficit, bottom) / q
    descendant_over_q = h_over_q - reset_over_q
    margin = value - budget
    slack = budget - h_over_q

    expected = {
        "q": Q(3176523, 25000000),
        "value": Q(
            200725034388752880197118033887607702918039504603683,
            223395363274892426079078092636160000000000000000000,
        ),
        "margin": Q(
            5714491495302498676679596453643417785239504603683,
            223395363274892426079078092636160000000000000000000,
        ),
        "reset_over_q": Q(
            58622378202530621387204787973,
            152536634460000000000000000000,
        ),
        "descendant_over_q": Q(
            9319613794564632698601357521105736737,
            51190344502039685438875740835676160000,
        ),
        "h_over_q": Q(
            884793664847325174104678035065147237189087444781,
            1562205337586660322231315333120000000000000000000,
        ),
        "slack": Q(
            478916425316663507856429919018519092410912555219,
            1562205337586660322231315333120000000000000000000,
        ),
    }
    observed = {
        "q": q,
        "value": value,
        "margin": margin,
        "reset_over_q": reset_over_q,
        "descendant_over_q": descendant_over_q,
        "h_over_q": h_over_q,
        "slack": slack,
    }
    for name, target in expected.items():
        if observed[name] != target:
            failures.append(f"witness fraction mismatch: {name}")
    if discrete != value:
        failures.append("polynomial and discrete-posterior majorants differ")
    if lifted_reset < reset_over_q:
        failures.append("Jensen reset direction failed")
    if not (margin > 0 and slack > 0 and value >= h_over_q):
        failures.append("witness sign or majorization failed")
    if len(poly) - 1 != 12:
        failures.append("unexpected Bellman polynomial degree")

    payload = {
        "claim": "fresh clean-room referee audit of frozen M152",
        "python": platform.python_version(),
        "seed": None,
        "predecessor_imports": False,
        "broad_scan": False,
        "immutable_hashes": observed_hashes,
        "doob_checks": doob_checks,
        "context_checks": context_checks,
        "witness": {
            "state_s_kappa_D_B": [s, kappa, deficit, bottom],
            "suffix_excess": excess,
            "q": record(q),
            "budget": record(budget),
            "bellman_degree": len(poly) - 1,
            "beta_jensen_value": record(value),
            "discrete_majorant": record(discrete),
            "positive_margin": record(margin),
            "jensen_reset": record(lifted_reset),
            "exact_reset_over_q": record(reset_over_q),
            "exact_descendant_over_q": record(descendant_over_q),
            "exact_H_over_q": record(h_over_q),
            "exact_budget_slack": record(slack),
        },
        "failure_count": len(failures),
        "failures": failures,
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.write_text(encoded)
    print(
        json.dumps(
            {
                "failure_count": len(failures),
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
