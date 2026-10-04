"""生成激活曲线解析采样表；运行 python3 figures/feedforward-curves.py。"""

from math import erf, exp, log1p, sqrt, tanh
from pathlib import Path


def sigmoid(z):
    return 1.0 / (1.0 + exp(-z))


def values(z):
    softplus = max(z, 0.0) + log1p(exp(-abs(z)))
    branches = (-z - 1.0, 0.5 * z, 2.0 * z - 1.0)
    return (z, sigmoid(z), tanh(z), min(1.0, max(0.0, z / 4.0 + 0.5)),
            min(1.0, max(-1.0, z)), z / (1.0 + abs(z)), max(0.0, z),
            z if z >= 0 else 0.1 * z, z if z >= 0 else 0.25 * z,
            z if z >= 0 else 0.2 * z, min(6.0, max(0.0, z)),
            z if z >= 0 else exp(z) - 1.0,
            1.0507009873554805 * (z if z >= 0 else 1.6732632423543772 * (exp(z) - 1.0)),
            softplus, z / 2.0, z * sigmoid(0.5 * z), z * sigmoid(z),
            z * sigmoid(5.0 * z), z * (1.0 + erf(z / sqrt(2.0))) / 2.0,
            z * tanh(softplus), z * min(6.0, max(0.0, z + 3.0)) / 6.0,
            *branches, max(branches), exp(z) / (exp(z) + 2.0), 1.0 / (exp(z) + 2.0))


def main():
    names = "z identity sigmoid tanh hardsigmoid hardtanh softsign relu leaky prelu rrelu relu6 elu selu softplus swish0 swish05 silu swish5 gelu mish hardswish branch1 branch2 branch3 maxout probability1 probability23"
    rows = [names + "\n"]
    for index in range(601):
        z = -4.0 + index / 50.0
        rows.append(f"{z:.8f} " + " ".join(f"{v:.12f}" for v in values(z)) + "\n")
    Path(__file__).with_name("feedforward-activation-curves.dat").write_text("".join(rows), encoding="utf-8")


if __name__ == "__main__":
    main()
