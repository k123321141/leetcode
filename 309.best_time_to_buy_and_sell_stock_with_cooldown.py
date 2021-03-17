from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int: # noqa
        self.prices = prices
        return self.dp(0, 0)

    @cache
    def dp(self, day: int, hold: bool) -> int:
        prices = self.prices
        if day >= len(prices) and hold:
            return float('-inf')
        elif day >= len(prices) and not hold:
            return 0
        if hold:
            return max(self.dp(day+2, False) + prices[day], self.dp(day+1, True))
        else:
            return max(self.dp(day+1, True) - prices[day], self.dp(day+1, False))
