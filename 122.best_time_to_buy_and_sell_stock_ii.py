class Solution:
    def maxProfit(self, prices: List[int]) -> int: # noqa
        '''
        find the all increasing arr
        '''
        if len(prices) <= 1:
            return 0
        # recusive
        low_idx = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                if low_idx < i-1:
                    profit += prices[i-1] - prices[low_idx]
                low_idx = i
        if low_idx < len(prices)-1:
            profit += prices[-1] - prices[low_idx]
        return profit
