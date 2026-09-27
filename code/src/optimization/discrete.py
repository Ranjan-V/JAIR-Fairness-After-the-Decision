"""Exact pseudo-polynomial solver for Theorem 12's welfare knapsack."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KnapsackResult:
    selected: tuple[int, ...]
    total_cost: int
    total_value: float


def knapsack_dynamic_program(costs, values, budget: int) -> KnapsackResult:
    costs = [int(c) for c in costs]
    values = [float(v) for v in values]
    if len(costs) != len(values) or budget < 0 or any(c < 0 for c in costs):
        raise ValueError("invalid knapsack instance")
    n = len(costs)
    dp = [[0.0] * (budget + 1) for _ in range(n + 1)]
    take = [[False] * (budget + 1) for _ in range(n + 1)]
    for i, (cost, value) in enumerate(zip(costs, values), start=1):
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost <= b and dp[i - 1][b - cost] + value > dp[i][b]:
                dp[i][b] = dp[i - 1][b - cost] + value
                take[i][b] = True
    selected = []
    b = budget
    for i in range(n, 0, -1):
        if take[i][b]:
            selected.append(i - 1)
            b -= costs[i - 1]
    selected.reverse()
    return KnapsackResult(tuple(selected), sum(costs[i] for i in selected), dp[n][budget])

