class Solution:
    def maxProfit(self, prices: List[int]) -> int: # noqa
        if len(prices) <= 1:
            return 0
        # arr version 22%
        '''
        cost = -1
        profit_arr = [0] * len(prices)
        for i, p in enumerate(prices):
            if cost == -1:
                cost = p
                profit_arr[i] = 0
            elif cost > p:
                cost = p
                profit_arr[i] = 0
            else:
                profit_arr[i] = p - cost
        return max(profit_arr)
        '''
        low = prices[0]
        profit = 0
        for p in prices[1:]:
            if p <= low:
                low = p
            else:
                diff = p - low
                profit = diff if diff > profit else profit

        return profit
