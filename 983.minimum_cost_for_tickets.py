from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:  # noqa
        self.days = days
        self.costs = costs
        self.min_cost = min(costs)
        return self.dp(0)

    @lru_cache
    def dp(self, idx: int) -> int:
        days = self.days
        costs = self.costs
        N = len(days)
        if idx == N - 1:
            return self.min_cost
        else:
            current = self.days[idx]
            next_idx = idx + 1

            # 1 day
            c1 = costs[0] + self.dp(next_idx) if next_idx < N else costs[0]
            # 7 day
            while next_idx < N and self.days[next_idx] < current + 7:
                next_idx += 1
            c7 = costs[1] + self.dp(next_idx) if next_idx < N else costs[1]
            # 7 day
            while next_idx < N and self.days[next_idx] < current + 30:
                next_idx += 1
            c30 = costs[2] + self.dp(next_idx) if next_idx < N else costs[2]

            ret = min(c1, c7, c30)
            return ret
