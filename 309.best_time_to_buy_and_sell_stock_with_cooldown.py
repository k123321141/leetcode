from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        return self.dp(0)

    @cache
    del dp(self, index: int) -> int:
        if len(prices) - index <= 1:
            return 0
        prices = self.prices
        low = prices[0]
        max_profit = 0
        for i in range(index, len(prices)):
            p = prices[i]
            if p <= low:
                low = p
            else:
                profit = p - low + self.dp(index+1)
                profit = diff if diff > profit else profit

        return profit

        
