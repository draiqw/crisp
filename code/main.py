"""Единая точка запуска: числа → results/, рисунок → slides/figures/.

    python main.py
"""

import experiment
import plot


def main():
    result = experiment.compute(experiment.load())
    table = experiment.save(result)
    figures = plot.draw(plot.load_result(table))
    print(f"results: {table}")
    for f in figures:
        print(f"figure:  {f}")


if __name__ == "__main__":
    main()
