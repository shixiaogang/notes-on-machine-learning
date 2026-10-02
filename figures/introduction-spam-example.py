#!/usr/bin/env python3
"""Generate the reproducible numbers used by Chapter 1's spam example."""

from __future__ import annotations

import csv
import math
from pathlib import Path


TRAIN = [
    ("tr01", 3, 2, 1),
    ("tr02", 2, 3, 1),
    ("tr03", 3, 1, 1),
    ("tr04", 2, 2, 1),
    ("tr05", 1, 3, 1),
    ("tr06", 0, 0, 0),
    ("tr07", 0, 1, 0),
    ("tr08", 1, 0, 0),
    ("tr09", 0, 2, 0),
    ("tr10", 1, 1, 0),
    ("tr11", 2, 0, 0),
    ("tr12", 0, 3, 0),
]

VALIDATION = [
    ("va01", 2, 1, 1),
    ("va02", 1, 2, 1),
    ("va03", 3, 0, 0),
    ("va04", 0, 2, 0),
    ("va05", 1, 1, 0),
    ("va06", 2, 2, 1),
]

TEST = [
    ("te01", 3, 2, 1),
    ("te02", 2, 1, 0),
    ("te03", 1, 3, 1),
    ("te04", 0, 0, 0),
    ("te05", 0, 2, 0),
    ("te06", 1, 0, 0),
    ("te07", 2, 0, 1),
    ("te08", 1, 2, 0),
]

NEW_MAIL = [
    ("new01", 2, 2),
    ("new02", 0, 1),
    ("new03", 1, 2),
]

LEARNING_RATE = 0.35
TRAINING_STEPS = 60
CANDIDATE_STEPS = (20, 40, 60)
THRESHOLD = 0.5


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def probability(parameters: list[float], x_1: int, x_2: int) -> float:
    bias, weight_1, weight_2 = parameters
    return sigmoid(bias + weight_1 * x_1 + weight_2 * x_2)


def mean_loss(data: list[tuple[str, int, int, int]], parameters: list[float]) -> float:
    total = 0.0
    for _, x_1, x_2, label in data:
        predicted = probability(parameters, x_1, x_2)
        total -= label * math.log(predicted) + (1 - label) * math.log(1 - predicted)
    return total / len(data)


def accuracy(data: list[tuple[str, int, int, int]], parameters: list[float]) -> float:
    correct = 0
    for _, x_1, x_2, label in data:
        predicted_label = int(probability(parameters, x_1, x_2) >= THRESHOLD)
        correct += predicted_label == label
    return correct / len(data)


def train() -> tuple[list[dict[str, float]], dict[int, list[float]]]:
    parameters = [0.0, 0.0, 0.0]
    history: list[dict[str, float]] = []
    checkpoints: dict[int, list[float]] = {}

    for step in range(TRAINING_STEPS + 1):
        history.append(
            {
                "step": step,
                "train_loss": mean_loss(TRAIN, parameters),
                "validation_loss": mean_loss(VALIDATION, parameters),
                "validation_accuracy": accuracy(VALIDATION, parameters),
            }
        )
        checkpoints[step] = parameters.copy()
        if step == TRAINING_STEPS:
            break

        gradients = [0.0, 0.0, 0.0]
        for _, x_1, x_2, label in TRAIN:
            error = probability(parameters, x_1, x_2) - label
            gradients[0] += error
            gradients[1] += error * x_1
            gradients[2] += error * x_2
        parameters = [
            value - LEARNING_RATE * gradient / len(TRAIN)
            for value, gradient in zip(parameters, gradients)
        ]

    return history, checkpoints


def main() -> None:
    history, checkpoints = train()
    selected_step = max(
        CANDIDATE_STEPS,
        key=lambda step: (history[step]["validation_accuracy"], -step),
    )
    selected = checkpoints[selected_step]

    output_path = Path(__file__).with_name("introduction-training-loss.csv")
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=("step", "train_loss", "validation_loss", "validation_accuracy"),
        )
        writer.writeheader()
        for row in history:
            writer.writerow(
                {
                    "step": int(row["step"]),
                    "train_loss": f'{row["train_loss"]:.6f}',
                    "validation_loss": f'{row["validation_loss"]:.6f}',
                    "validation_accuracy": f'{row["validation_accuracy"]:.6f}',
                }
            )

    print(f"selected_step={selected_step}")
    print("parameters=" + ",".join(f"{value:.6f}" for value in selected))
    for name, data in (("validation", VALIDATION), ("test", TEST)):
        print(f"{name}_accuracy={accuracy(data, selected):.6f}")
        for sample_id, x_1, x_2, label in data:
            predicted = probability(selected, x_1, x_2)
            print(f"{sample_id}: x=({x_1},{x_2}) y={label} p={predicted:.6f} pred={int(predicted >= THRESHOLD)}")
    for sample_id, x_1, x_2 in NEW_MAIL:
        predicted = probability(selected, x_1, x_2)
        print(f"{sample_id}: x=({x_1},{x_2}) p={predicted:.6f} pred={int(predicted >= THRESHOLD)}")


if __name__ == "__main__":
    main()
