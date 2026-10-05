"""强化学习前三章的教学网格：用有理数精确求解价值和占用度量。

运行：python3 figures/rl-grid-reference.py
输出为 JSON，可用于核对 TikZ 图和正文算例。所有输入均为教学假设。
终点只有 stop 动作，终止后的吸收占用仍计入归一化分布。
"""

from fractions import Fraction as F
import json

GAMMA = F(9, 10)
START, GOAL, WALL = (1, 1), (4, 3), (2, 2)
STATES = [(x, y) for y in range(1, 4) for x in range(1, 5) if (x, y) != WALL]
INDEX = {state: index for index, state in enumerate(STATES)}
DIRECTIONS = [("up", (0, 1)), ("right", (1, 0)), ("down", (0, -1)), ("left", (-1, 0))]


def destination(state, delta):
    return state[0] + delta[0], state[1] + delta[1]


def actions(state):
    if state == GOAL:
        return ["stop"]
    return [name for name, delta in DIRECTIONS if destination(state, delta) in INDEX]


def transition(state, action):
    if action not in actions(state):
        raise ValueError("意图方向不合法")
    if state == GOAL:
        return {GOAL: F(1)}
    intended = next(i for i, (name, _) in enumerate(DIRECTIONS) if name == action)
    result = {}
    for offset, probability in [(0, F(4, 5)), (-1, F(1, 10)), (1, F(1, 10))]:
        successor = destination(state, DIRECTIONS[(intended + offset) % 4][1])
        if successor not in INDEX:
            successor = state
        result[successor] = result.get(successor, F(0)) + probability
    return result


def reward(state, successor):
    return F(0) if state == GOAL else F(1) if successor == GOAL else F(-1, 25)


def solve(matrix, rhs):
    """带主元选择的有理数 Gauss–Jordan 消元，不引入浮点求逆误差。"""
    n = len(rhs)
    rows = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if rows[row][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [value / scale for value in rows[col]]
        for row in range(n):
            if row != col:
                scale = rows[row][col]
                rows[row] = [a - scale * b for a, b in zip(rows[row], rows[col])]
    return [row[-1] for row in rows]


def model(policy):
    n = len(STATES)
    matrix = [[F(0) for _ in STATES] for _ in STATES]
    rewards = [F(0) for _ in STATES]
    for i, state in enumerate(STATES):
        for action, weight in policy[state].items():
            for successor, probability in transition(state, action).items():
                matrix[i][INDEX[successor]] += weight * probability
                rewards[i] += weight * probability * reward(state, successor)
    assert all(sum(row) == 1 for row in matrix)
    return matrix, rewards


def evaluate(policy):
    matrix, rewards = model(policy)
    system = [[F(i == j) - GAMMA * probability for j, probability in enumerate(row)]
              for i, row in enumerate(matrix)]
    return solve(system, rewards)


def qvalue(state, action, values):
    return sum(probability * (reward(state, successor) + GAMMA * values[INDEX[successor]])
               for successor, probability in transition(state, action).items())


def occupancy(policy):
    matrix, _ = model(policy)
    system = [[F(i == j) - GAMMA * matrix[j][i] for j in range(len(STATES))]
              for i in range(len(STATES))]
    distribution = solve(system, [(1 - GAMMA) * F(state == START) for state in STATES])
    assert sum(distribution) == 1 and all(value >= 0 for value in distribution)
    return distribution


def compute():
    uniform = {state: {a: F(1, len(actions(state))) for a in actions(state)} for state in STATES}
    chosen = {state: actions(state)[0] for state in STATES}
    iterations = 0
    while True:
        policy = {state: {chosen[state]: F(1)} for state in STATES}
        optimal_values = evaluate(policy)
        improved = {}
        for state in STATES:
            scores = {a: qvalue(state, a, optimal_values) for a in actions(state)}
            maximum = max(scores.values())
            # 并列最优时保留原动作，避免无意义的策略切换。
            improved[state] = chosen[state] if scores[chosen[state]] == maximum else max(scores, key=scores.get)
        iterations += 1
        if improved == chosen:
            break
        chosen = improved
    uniform_values = evaluate(uniform)
    uniform_d, optimal_d = occupancy(uniform), occupancy(policy)
    for candidate, values, distribution in [
        (uniform, uniform_values, uniform_d), (policy, optimal_values, optimal_d)
    ]:
        _, rewards = model(candidate)
        assert values[INDEX[START]] == sum(d * r for d, r in zip(distribution, rewards)) / (1 - GAMMA)
        assert all(values[i] == sum(weight * qvalue(state, action, values)
                                   for action, weight in candidate[state].items())
                   for i, state in enumerate(STATES))
    assert all(optimal_values[i] == max(qvalue(state, a, optimal_values) for a in actions(state))
               for i, state in enumerate(STATES))
    return {
        "source": "教学网格；有理数精确策略评价、策略迭代和占用流方程",
        "gamma": float(GAMMA),
        "policy_iterations": iterations,
        "exact_bellman_and_flow_checks": True,
        "rows": [
            {
                "state": state,
                "uniform_value": float(uniform_values[i]),
                "optimal_value": float(optimal_values[i]),
                "optimal_action": chosen[state],
                "uniform_occupancy": float(uniform_d[i]),
                "optimal_occupancy": float(optimal_d[i]),
            }
            for i, state in enumerate(STATES)
        ],
    }


if __name__ == "__main__":
    print(json.dumps(compute(), ensure_ascii=False, indent=2))
