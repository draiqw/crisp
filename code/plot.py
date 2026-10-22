"""Визуализация: читает сохранённые результаты и строит главный рисунок.

Вычисления не перезапускаются: можно менять стиль, не трогая experiment.py.
"""

import csv

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import config  # noqa: E402

COLORS = {
    "baseline": "#9E9E9E",
    "gsm8k": "#90CAF9",
    "dapo_math": "#64B5F6",
    "deepmath": "#1E88E5",
    "crisp_stem": "#E67E22",
}


def load_result(path=None):
    path = path or config.RESULTS / "main_result.csv"
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def draw(result, out_dir=config.FIGURES):
    out_dir.mkdir(parents=True, exist_ok=True)
    benches = list(config.BENCHMARKS)
    datasets = list(config.DATASETS)
    cell = {(r["grpo_data"], r["benchmark"]): r for r in result}

    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    width = 0.16
    x = np.arange(len(benches))
    for i, d in enumerate(datasets):
        acc = [float(cell[d, b]["acc_at_1"]) for b in benches]
        err = [float(cell[d, b]["std"]) for b in benches]
        bars = ax.bar(x + (i - 2) * width, acc, width, yerr=err, capsize=2,
                      color=COLORS[d], edgecolor="black" if d == config.OURS else "none",
                      linewidth=1.2, label=config.DATASETS[d], error_kw={"linewidth": 0.8})
        if d == config.OURS:
            for rect, v, e in zip(bars, acc, err):
                ax.text(rect.get_x() + rect.get_width() / 2, v + e + 1.5, f"{v:.1f}",
                        ha="center", va="bottom", fontsize=9, fontweight="bold")

    ax.set_xticks(x, [config.BENCHMARKS[b] for b in benches])
    ax.set_ylabel("acc@1, %")
    ax.set_ylim(0, 105)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(title="Данные GRPO", fontsize=9, title_fontsize=9, ncol=5,
              loc="upper center", bbox_to_anchor=(0.5, 1.2), frameon=False)
    fig.tight_layout()

    paths = []
    for ext in ("pdf", "png"):
        p = out_dir / f"oslide_main.{ext}"
        fig.savefig(p, dpi=200, bbox_inches="tight")
        paths.append(p)
    plt.close(fig)
    return paths


if __name__ == "__main__":
    print(*draw(load_result()), sep="\n")
