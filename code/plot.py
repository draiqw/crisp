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
    "baseline": "#BDBDBD",
    "gsm8k": "#90CAF9",
    "dapo_math": "#42A5F5",
    "deepmath": "#1565C0",
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
    cell = {(r["policy"], r["grpo_data"], r["benchmark"]): r for r in result}

    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(len(config.POLICIES), 1, figsize=(12, 4.8), sharex=True)
    width = 0.16
    x = np.arange(len(benches)) + np.where(np.array(benches) == "mean", 0.4, 0.0)

    for ax, (policy, title) in zip(axes, config.POLICIES.items()):
        for i, d in enumerate(datasets):
            acc = [float(cell[policy, d, b]["acc_at_1"]) for b in benches]
            err = [float(cell[policy, d, b]["std"]) for b in benches]
            ax.bar(x + (i - 2) * width, acc, width, yerr=err, capsize=1.5,
                   color=COLORS[d], label=config.DATASETS[d],
                   error_kw={"linewidth": 0.6, "ecolor": "#424242"})
        mean_x = x[benches.index("mean")]
        ax.axvline(mean_x - 0.7, color="#9E9E9E", linewidth=0.6, linestyle="--")
        ax.set_title(title, loc="left", fontsize=12, fontweight="bold")
        ax.set_ylabel("acc@1, %")
        ax.set_ylim(0, 115)
        ax.set_yticks(range(0, 101, 20))
        ax.grid(axis="y", linewidth=0.3, alpha=0.6)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)

    axes[-1].set_xticks(x, [config.BENCHMARKS[b] for b in benches], fontsize=11)
    axes[0].legend(title="Данные для GRPO", fontsize=11, title_fontsize=11, ncol=5,
                   loc="lower center", bbox_to_anchor=(0.5, 1.12), frameon=False)
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
