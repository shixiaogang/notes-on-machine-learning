#!/usr/bin/env python3
"""Exact data for dim-diffusion-walk.tex; Python standard library only.

Run from any directory:
  python3 figures/dim-diffusion-walk.py
  python3 figures/dim-diffusion-walk.py --check

The default output contains the six-decimal TikZ cell data and diagnostics.
--check compares all embedded cells with freshly computed rational results.
Node order: L1,L2,L3,R1,R2,R3. All within-group entries, including the
diagonal, equal 1. The only bridge is K[L3,R1]=K[R1,L3]=3/20.
There is no density reweighting (alpha=0). P[i,j]=K[i,j]/sum_j K[i,j].
Powers use exact Fraction matrix loops, not simulated sample paths.
"""

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
import re


N = 6
TIMES = (1, 4, 64)
SOURCES = (0, 5)
ZERO = Fraction(0)
ONE = Fraction(1)


def matmul(left, right):
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(N)), ZERO)
            for j in range(N)
        ]
        for i in range(N)
    ]


def decimal(value, places=6):
    with localcontext() as context:
        context.prec = 40
        return format(Decimal(value.numerator) / Decimal(value.denominator),
                      f".{places}f")


def compute():
    weights = [
        [ONE if i // 3 == j // 3 else ZERO for j in range(N)]
        for i in range(N)
    ]
    weights[2][3] = weights[3][2] = Fraction(3, 20)
    degrees = [sum(row, ZERO) for row in weights]
    transition = [
        [value / degrees[i] for value in row]
        for i, row in enumerate(weights)
    ]
    stationary = [value / sum(degrees, ZERO) for value in degrees]
    assert stationary == [Fraction(value, 122) for value in (20, 20, 21, 21, 20, 20)]
    assert all(sum(row, ZERO) == ONE for row in transition)
    for j in range(N):
        assert sum((stationary[i] * transition[i][j] for i in range(N)), ZERO) == stationary[j]
        for i in range(N):
            assert stationary[i] * transition[i][j] == stationary[j] * transition[j][i]

    power = [[Fraction(i == j) for j in range(N)] for i in range(N)]
    snapshots = {}
    for step in range(1, max(TIMES) + 1):
        power = matmul(power, transition)
        assert all(sum(row, ZERO) == ONE for row in power)
        assert all(value >= ZERO for row in power for value in row)
        if step in TIMES:
            snapshots[step] = power
            assert power[0] == list(reversed(power[5]))
    assert snapshots[1][0] == [Fraction(1, 3)] * 3 + [ZERO] * 3
    assert snapshots[1][5] == [ZERO] * 3 + [Fraction(1, 3)] * 3
    return snapshots, stationary


def cell_data(snapshots):
    return [
        (str(panel), str(row), str(col), decimal(snapshots[step][source][col]))
        for panel, step in enumerate(TIMES)
        for row, source in enumerate(SOURCES)
        for col in range(N)
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    snapshots, stationary = compute()
    cells = cell_data(snapshots)
    if args.check:
        source = Path(__file__).with_suffix(".tex").read_text(encoding="utf-8")
        stored = re.findall(
            r"^\s+([0-2])/([01])/([0-5])/([0-9]+\.[0-9]{6}),?\s*$",
            source, re.MULTILINE,
        )
        assert stored == cells, "Embedded TikZ cells differ from exact matrix powers"
        print("PASS: all 36 cells, row sums, reflection, stationarity and detailed balance")
    else:
        print("% panel/row/column/probability; rounded once from exact fractions")
        for index, cell in enumerate(cells):
            print("    " + "/".join(cell) + ("," if index + 1 < len(cells) else ""))

    print("stationary = (" + ", ".join(map(str, stationary)) + ")")
    for step in TIMES:
        left, right = (snapshots[step][source] for source in SOURCES)
        cross_mass = sum(left[3:], ZERO)
        total_variation = sum((abs(a - b) for a, b in zip(left, right)), ZERO) / 2
        to_stationary = sum((abs(a - b) for a, b in zip(left, stationary)), ZERO) / 2
        distance_squared = sum(
            ((a - b) ** 2 / pi for a, b, pi in zip(left, right, stationary)), ZERO
        )
        print(f"t={step}: opposite-group mass={decimal(cross_mass, 9)}, "
              f"TV(L1,R3)={decimal(total_variation, 9)}, "
              f"TV(L1,pi)={decimal(to_stationary, 9)}, "
              f"D_t^2(L1,R3)={decimal(distance_squared, 9)}")
    # Finite-time differences remain; the connected graph with self-loops
    # implies convergence to pi only as t tends to infinity.
    assert snapshots[64][0] != stationary


if __name__ == "__main__":
    main()
