#!/usr/bin/env python3
"""Aggregate edge-shift JSONL results and fit exploratory scaling models.

The analysis deliberately labels all regressions as empirical.  Censored
trials contribute their cutoff to the restricted mean, E[min(tau, cutoff)].
Rows with more than 5% censoring are excluded from log-linear fits.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


def percentile(values: Sequence[float], probability: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    position = probability * (len(ordered) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return ordered[lower] + fraction * (ordered[upper] - ordered[lower])


def read_records(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"invalid JSON at {path}:{line_number}: {error}") from error


def summarize_trials(trials: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    observed = [float(trial["observed_steps"]) for trial in trials]
    hits = [float(trial["hit_step"]) for trial in trials if trial["hit"]]
    hit_count = len(hits)
    count = len(trials)
    return {
        "trial_count": count,
        "hit_count": hit_count,
        "censored_count": count - hit_count,
        "hit_rate": hit_count / count if count else None,
        "censor_fraction": (count - hit_count) / count if count else None,
        "restricted_mean_steps": statistics.fmean(observed) if observed else None,
        "conditional_mean_hit_steps": statistics.fmean(hits) if hits else None,
        "conditional_median_hit_steps": percentile(hits, 0.5),
        "conditional_p90_hit_steps": percentile(hits, 0.9),
        "conditional_p99_hit_steps": percentile(hits, 0.99),
        "max_steps": max(int(trial["max_steps"]) for trial in trials) if trials else None,
    }


def flatten_graph_summary(record: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "setting_id": record["setting_id"],
        "graph_id": record["graph_id"],
        "generator": record["generator"],
        "vertex_count": record["vertex_count"],
        "edge_count": record["edge_count"],
        "component_count": record["component_count"],
        "cycle_rank": record["cycle_rank"],
        "bridge_count": record["bridge_count"],
        "girth": record["girth"],
        "triangle_count": record["triangle_count"],
        "min_degree": record["min_degree"],
        "max_degree": record["max_degree"],
        "ordered_wedge_count": record["ordered_wedge_count"],
        "fundamental_cycle_basis_mean_length": record["fundamental_cycle_basis_mean_length"],
        "fundamental_cycle_basis_min_length": record["fundamental_cycle_basis_min_length"],
        "fundamental_cycle_basis_max_length": record["fundamental_cycle_basis_max_length"],
        "simple_cycle_count_exact": record["simple_cycle_count_exact"],
        "simple_cycle_mean_length_exact": record["simple_cycle_mean_length_exact"],
        "simple_cycle_min_length_exact": record["simple_cycle_min_length_exact"],
        "simple_cycle_max_length_exact": record["simple_cycle_max_length_exact"],
        "simple_cycle_length_histogram_exact": json.dumps(
            record["simple_cycle_length_histogram_exact"], sort_keys=True, separators=(",", ":")
        ) if record["simple_cycle_length_histogram_exact"] is not None else None,
        "cycle_enumeration_skipped": record["simple_cycle_enumeration_skipped_reason"] is not None,
    }


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def solve_linear_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(vector)
    augmented = [row[:] + [value] for row, value in zip(matrix, vector)]
    for column in range(n):
        pivot = max(range(column, n), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-12:
            raise ValueError("singular design matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    left - factor * right
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return [augmented[row][-1] for row in range(n)]


def log_linear_model(
    rows: Sequence[Mapping[str, Any]],
    *,
    feature_names: Sequence[str],
    model_name: str,
) -> dict[str, Any]:
    usable = []
    for row in rows:
        y = row.get("restricted_mean_steps")
        if not y or y <= 0 or float(row.get("censor_fraction") or 0.0) > 0.05:
            continue
        features = [row.get(name) for name in feature_names]
        if any(value is None or float(value) <= 0 for value in features):
            continue
        usable.append((math.log(float(y)), [1.0] + [math.log(float(value)) for value in features]))

    parameter_count = len(feature_names) + 1
    result: dict[str, Any] = {
        "model": model_name,
        "interpretation": "exploratory log-linear fit; coefficients are empirical exponents, not a theorem",
        "response": "log(restricted_mean_steps)",
        "features": [f"log({name})" for name in feature_names],
        "row_count": len(usable),
        "excluded_if_censor_fraction_above": 0.05,
    }
    if len(usable) <= parameter_count:
        result["status"] = "insufficient_rows"
        return result

    xtx = [[0.0] * parameter_count for _ in range(parameter_count)]
    xty = [0.0] * parameter_count
    for y, x in usable:
        for left in range(parameter_count):
            xty[left] += x[left] * y
            for right in range(parameter_count):
                xtx[left][right] += x[left] * x[right]
    try:
        coefficients = solve_linear_system(xtx, xty)
    except ValueError as error:
        result["status"] = "singular"
        result["reason"] = str(error)
        return result

    responses = [item[0] for item in usable]
    predictions = [sum(coefficient * value for coefficient, value in zip(coefficients, x)) for _, x in usable]
    mean_response = statistics.fmean(responses)
    residual_sum = sum((response - prediction) ** 2 for response, prediction in zip(responses, predictions))
    total_sum = sum((response - mean_response) ** 2 for response in responses)
    names = ["intercept"] + [f"log({name})" for name in feature_names]
    result.update({
        "status": "ok",
        "coefficients": dict(zip(names, coefficients)),
        "r_squared": 1.0 - residual_sum / total_sum if total_sum else None,
    })
    return result


def analyze(input_path: Path, output_directory: Path) -> dict[str, Any]:
    graph_summaries: dict[str, dict[str, Any]] = {}
    trials_by_graph: dict[str, list[dict[str, Any]]] = defaultdict(list)
    completed_graphs: set[str] = set()

    for record in read_records(input_path):
        record_type = record.get("record_type")
        if record_type == "graph_summary":
            graph_summaries[record["graph_id"]] = record
        elif record_type == "walk_trial":
            trials_by_graph[record["graph_id"]].append(record)
        elif record_type == "graph_complete":
            completed_graphs.add(record["graph_id"])

    graph_rows: list[dict[str, Any]] = []
    for graph_id in sorted(graph_summaries):
        if graph_id not in completed_graphs:
            continue
        row = flatten_graph_summary(graph_summaries[graph_id])
        row.update(summarize_trials(trials_by_graph[graph_id]))
        graph_rows.append(row)

    trials_by_setting: dict[str, list[dict[str, Any]]] = defaultdict(list)
    graph_rows_by_setting: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for graph_id in completed_graphs:
        for trial in trials_by_graph.get(graph_id, []):
            trials_by_setting[trial["setting_id"]].append(trial)
    for row in graph_rows:
        graph_rows_by_setting[row["setting_id"]].append(row)

    setting_rows: list[dict[str, Any]] = []
    for setting_id in sorted(trials_by_setting):
        rows = graph_rows_by_setting[setting_id]
        representative = rows[0]
        summary = {
            "setting_id": setting_id,
            "generator": representative["generator"],
            "graph_count": len(rows),
            "vertex_count_mean": statistics.fmean(float(row["vertex_count"]) for row in rows),
            "edge_count_mean": statistics.fmean(float(row["edge_count"]) for row in rows),
            "cycle_rank_mean": statistics.fmean(float(row["cycle_rank"]) for row in rows),
            "girth_mean": statistics.fmean(float(row["girth"]) for row in rows if row["girth"] is not None),
            "basis_cycle_mean_length_mean": statistics.fmean(
                float(row["fundamental_cycle_basis_mean_length"])
                for row in rows
                if row["fundamental_cycle_basis_mean_length"] is not None
            ),
            "simple_cycle_count_exact_mean": (
                statistics.fmean(float(row["simple_cycle_count_exact"]) for row in rows)
                if all(row["simple_cycle_count_exact"] is not None for row in rows)
                else None
            ),
            "simple_cycle_mean_length_exact_mean": (
                statistics.fmean(float(row["simple_cycle_mean_length_exact"]) for row in rows)
                if all(row["simple_cycle_mean_length_exact"] is not None for row in rows)
                else None
            ),
        }
        summary.update(summarize_trials(trials_by_setting[setting_id]))
        setting_rows.append(summary)

    output_directory.mkdir(parents=True, exist_ok=True)
    write_csv(output_directory / "graph_summaries.csv", graph_rows)
    write_csv(output_directory / "setting_summaries.csv", setting_rows)

    models = [
        log_linear_model(
            graph_rows,
            feature_names=["edge_count", "cycle_rank", "fundamental_cycle_basis_mean_length"],
            model_name="scalable_cycle_rank_and_basis_length",
        ),
        log_linear_model(
            graph_rows,
            feature_names=["edge_count", "simple_cycle_count_exact", "simple_cycle_mean_length_exact"],
            model_name="exact_simple_cycle_count_and_length",
        ),
    ]
    models_by_generator = {}
    for generator in sorted({str(row["generator"]) for row in graph_rows}):
        generator_rows = [row for row in graph_rows if row["generator"] == generator]
        models_by_generator[generator] = [
            log_linear_model(
                generator_rows,
                feature_names=["edge_count", "cycle_rank", "fundamental_cycle_basis_mean_length"],
                model_name=f"{generator}:scalable_cycle_rank_and_basis_length",
            ),
            log_linear_model(
                generator_rows,
                feature_names=["edge_count", "simple_cycle_count_exact", "simple_cycle_mean_length_exact"],
                model_name=f"{generator}:exact_simple_cycle_count_and_length",
            ),
        ]
    summary = {
        "input": str(input_path),
        "completed_graph_count": len(graph_rows),
        "setting_count": len(setting_rows),
        "trial_count": sum(len(trials) for trials in trials_by_graph.values()),
        "outputs": {
            "graph_summaries": str(output_directory / "graph_summaries.csv"),
            "setting_summaries": str(output_directory / "setting_summaries.csv"),
        },
        "models": models,
        "models_by_generator": models_by_generator,
        "censoring_note": "restricted_mean_steps is E[min(tau,max_steps)]; conditional means omit censored trials",
    }
    (output_directory / "analysis_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return summary


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="results JSONL")
    parser.add_argument("--out-dir", type=Path, default=Path("analysis"))
    return parser.parse_args(argv)


if __name__ == "__main__":
    arguments = parse_args()
    print(json.dumps(analyze(arguments.input.resolve(), arguments.out_dir.resolve()), indent=2, sort_keys=True))
