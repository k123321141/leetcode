from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int: # noqa
        self.prices = prices
        return self.dp(0)

    @cache
    def dp(self, index: int) -> int:
        prices = self.prices
        if len(prices) - index <= 1:
            return 0
        prices = self.prices
        low = prices[index]
        max_profit = 0
        for i in range(index, len(prices)):
            p = prices[i]
            if p <= low:
                low = p
            else:
                profit = p - low + self.dp(i+2)
                max_profit = max(max_profit, profit)
        return max_profit
