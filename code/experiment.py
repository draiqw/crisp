"""Вычисления: читает итоговый eval и сохраняет таблицу для рисунка.

Вход — `data/eval_broad.csv`: acc@1 и acc@k (%) лучшего in-domain чекпоинта
каждого GRPO-рана на Qwen3-14B (Base/Instruct), протокол avg@3 / pass@3, T=0.6.
Выход — `results/main_result.csv`: для каждой политики и каждых данных GRPO
acc@1 по бенчмаркам и их среднее, разница с исходной моделью и шум ±std.
"""

import csv
import math
from collections import defaultdict

import config


def load(path=config.DATA):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def noise_std(acc_percent, n_problems):
    """Биномиальный шум доли решённых задач, в процентных пунктах."""
    p = acc_percent / 100
    return 100 * math.sqrt(p * (1 - p) / n_problems)


def compute(rows):
    benches = [b for b in config.BENCHMARKS if b != "mean"]
    acc = defaultdict(dict)  # (policy, data) -> {bench: acc@1}
    step = {}
    for r in rows:
        if r["benchmark"] in benches:
            acc[r["policy"], r["grpo_data"]][r["benchmark"]] = float(r["acc_at_1"])
            step[r["policy"], r["grpo_data"]] = r["step"]

    out = []
    for policy in config.POLICIES:
        base = acc[policy, "baseline"]
        for data in config.DATASETS:
            cur = acc[policy, data]
            stds = {b: noise_std(cur[b], config.N_PROBLEMS[b]) for b in benches}
            cur = dict(cur, mean=sum(cur[b] for b in benches) / len(benches))
            ref = dict(base, mean=sum(base[b] for b in benches) / len(benches))
            # шум среднего: независимые бенчмарки, std суммы / число бенчмарков
            stds["mean"] = math.sqrt(sum(s * s for s in stds.values())) / len(benches)
            for b in config.BENCHMARKS:
                out.append({
                    "policy": policy,
                    "grpo_data": data,
                    "step": step[policy, data],
                    "benchmark": b,
                    "acc_at_1": round(cur[b], 1),
                    "delta_vs_baseline": round(cur[b] - ref[b], 1),
                    "std": round(stds[b], 2),
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
