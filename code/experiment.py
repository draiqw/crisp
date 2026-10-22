"""Вычисления: читает итоговый eval и сохраняет таблицу для рисунка.

Вход — `data/eval_broad.csv`: acc@1 и acc@k (%) лучшего in-domain чекпоинта
каждого GRPO-рана на Qwen3-14B (Base/Instruct), протокол avg@3 / pass@3, T=0.6.
Выход — `results/main_result.csv`: acc@1, разница с baseline и шум ±std.
"""

import csv
import math

import config


def load(path=config.DATA):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def noise_std(acc_percent, n_problems):
    """Биномиальный шум доли решённых задач, в процентных пунктах."""
    p = acc_percent / 100
    return 100 * math.sqrt(p * (1 - p) / n_problems)


def compute(rows, policy=config.POLICY):
    rows = [r for r in rows if r["policy"] == policy]
    baseline = {r["benchmark"]: float(r["acc_at_1"]) for r in rows if r["grpo_data"] == "baseline"}
    out = []
    for r in rows:
        bench = r["benchmark"]
        if bench not in config.BENCHMARKS:
            continue
        acc = float(r["acc_at_1"])
        out.append({
            "grpo_data": r["grpo_data"],
            "step": r["step"],
            "benchmark": bench,
            "acc_at_1": acc,
            "delta_vs_baseline": round(acc - baseline[bench], 1),
            "std": round(noise_std(acc, config.N_PROBLEMS[bench]), 2),
        })
    return out


def save(result, path=None):
    path = path or config.RESULTS / "main_result.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(result[0]))
        w.writeheader()
        w.writerows(result)
    return path
