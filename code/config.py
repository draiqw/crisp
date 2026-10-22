"""Все параметры эксперимента O-slide в одном месте."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "eval_broad.csv"
RESULTS = ROOT / "results"
FIGURES = ROOT.parent / "slides" / "figures"

# Политика, для которой строится главный рисунок
POLICY = "instruct"

# Бенчмарки на рисунке и их подписи
BENCHMARKS = {
    "math_500": "MATH-500",
    "aime_2024": "AIME-24",
    "aime_2025": "AIME-25",
    "gpqa_diamond": "GPQA-D",
}

# Число задач в бенчмарке: нужно для оценки шума std = sqrt(p(1-p)/N)
N_PROBLEMS = {
    "gsm8k": 1319, "gsm8k_ru": 1319,
    "math_500": 500, "math_500_ru": 500,
    "aime_2024": 30, "aime_2025": 30,
    "gpqa_diamond": 198, "mmlu_stem": 2287, "rummlu_stem": 2273,
}

# Обучающие данные GRPO: порядок на рисунке и подписи
DATASETS = {
    "baseline": "без дообучения",
    "gsm8k": "GSM8K",
    "dapo_math": "DAPO-Math",
    "deepmath": "DeepMath",
    "crisp_stem": "CRISP (наш)",
}
OURS = "crisp_stem"
