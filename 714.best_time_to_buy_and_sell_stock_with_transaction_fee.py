from functools import cache


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int: # noqa
        self.prices = prices
        self.fee = fee
        return self.dp(0, 0)

    @cache
    def dp(self, day: int, hold: bool) -> int:
        prices = self.prices
        fee = self.fee
        if day >= len(prices) and hold:
            return float('-inf')
        elif day >= len(prices) and not hold:
            return 0
        if hold:
            return max(self.dp(day+1, False) + prices[day] - fee, self.dp(day+1, True))
        else:
            return max(self.dp(day+1, True) - prices[day], self.dp(day+1, False))
