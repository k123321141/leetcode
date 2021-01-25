class Solution:
    def maxProfit(self, prices: List[int]) -> int: # noqa
        '''
        1. Construct profit arrary for buy-first-sell-last process.
        2. Construct profit arrary for sell-first-buy-last process.
        3. Find the best profit in this 2 arrays.
        O(N)
        '''
        if len(prices) <= 1:
            return 0
        # buy-first-sell-last
        buy = float('inf')
        max_profit = 0
        forward_profit_arr = []
        for i, p in enumerate(prices):
            if buy > p:
                buy = p
                profit = 0
            else:
                profit = p - buy
            max_profit = profit if profit > max_profit else max_profit
            forward_profit_arr.append(max_profit)
        # sell-first-buy-last
        sell = float('-inf')
        max_profit = 0
        max_total = 0
        for i in range(len(prices)-1, -1, -1):
            p = prices[i]
            if sell < p:
                sell = p
                profit = 0
            else:
                profit = sell - p
            max_profit = profit if profit > max_profit else max_profit
            # find best split index
            total = max_profit
            if i > 0:
                total += forward_profit_arr[i-1]
            max_total = total if total > max_total else max_total
        return max_total
