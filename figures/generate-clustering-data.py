"""生成聚类章原理图的确定性教学数据；仅依赖 Python 标准库。

运行：python3 figures/generate-clustering-data.py
各数据表由对应 TikZ/PGFPlots 文件读取，不表示真实数据实验。
"""

from pathlib import Path
import heapq
import math


ROOT = Path(__file__).resolve().parent


def write_table(name, header, rows):
    def cell(value):
        return "nan" if not math.isfinite(value) else f"{value:.9g}"
    text = header + "\n"
    text += "\n".join(" ".join(cell(v) for v in row) for row in rows) + "\n"
    (ROOT / name).write_text(text, encoding="utf-8")


def normal(x, mean, sigma):
    return math.exp(-0.5 * ((x - mean) / sigma) ** 2) / (
        sigma * math.sqrt(2 * math.pi)
    )


def make_density_data():
    samples = [-2.5, -2.0, -1.5, 1.5, 2.0, 2.5]
    def kde(y, h):
        return sum(normal(y, x, h) for x in samples) / len(samples)
    grid = [-4 + i / 40 for i in range(321)]
    write_table("clustering-kde.dat", "x narrow broad",
                [(x, kde(x, 0.6), kde(x, 2.4)) for x in grid])
    left, right = -0.8, 0.8
    rows = []
    for t in range(5):
        rows.append((t, left, kde(left, 0.6), right, kde(right, 0.6)))
        def advance(y):
            weights = [math.exp(-((y - x) / 0.6) ** 2 / 2) for x in samples]
            return sum(w * x for w, x in zip(weights, samples)) / sum(weights)
        left, right = advance(left), advance(right)
    assert all(rows[t + 1][2] >= rows[t][2] for t in range(4))
    write_table("clustering-mean-shift-path.dat",
                "step left fleft right fright", rows)

    rows = []
    for x in grid:
        first, second = normal(x, -1, 1) / 2, normal(x, 1, 1) / 2
        mixture = first + second
        rows.append((x, first, second, mixture, first / mixture, second / mixture))
    assert abs(rows[160][4] - 0.5) < 1e-12
    write_table("clustering-gmm.dat",
                "x first second mixture gammaone gammatwo", rows)


def make_optics_data():
    # 三组不同间距的一维样本及一个孤立点；m=3 含自身，eps_max=1.1。
    samples = [0.15 * i for i in range(7)]
    samples += [4 + 0.4 * i for i in range(6)]
    samples += [8 + 0.1 * i for i in range(9)]
    samples += [12.0]
    n, eps, m = len(samples), 1.1, 3
    distance = [[abs(x - y) for y in samples] for x in samples]
    core = [sorted(row)[m - 1] if sorted(row)[m - 1] <= eps
            else math.inf for row in distance]
    reach = [math.inf] * n
    done, ordering = set(), []
    for start in range(n):
        if start in done:
            continue
        heap = [(math.inf, start)]
        while heap:
            value, i = heapq.heappop(heap)
            if i in done or value != reach[i]:
                continue
            done.add(i)
            ordering.append(i)
            if not math.isfinite(core[i]):
                continue
            for j in range(n):
                if j in done or distance[i][j] > eps:
                    continue
                candidate = max(core[i], distance[i][j])
                if candidate < reach[j]:
                    reach[j] = candidate
                    heapq.heappush(heap, (candidate, j))
    assert len(ordering) == n
    assert sum(math.isinf(reach[i]) for i in ordering) == 4
    rows = [(j + 1, samples[i], reach[i], core[i],
             1.05 if math.isinf(reach[i]) else math.nan)
            for j, i in enumerate(ordering)]
    write_table("clustering-optics.dat", "order x reach core restart", rows)
    print("OPTICS ordering:", [round(samples[i], 2) for i in ordering])


if __name__ == "__main__":
    make_density_data()
    make_optics_data()
    print("Generated KDE, Mean Shift trajectories, GMM, and OPTICS tables.")
