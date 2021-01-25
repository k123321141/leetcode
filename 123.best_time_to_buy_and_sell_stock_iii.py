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
        forward_profit_arr = [0] * len(prices)
        for i, p in enumerate(prices):
            if buy > p:
                buy = p
                profit = 0
            else:
                profit = p - buy
            max_profit = profit if profit > max_profit else max_profit
            forward_profit_arr[i] = max_profit
        # sell-first-buy-last
        sell = float('-inf')
        max_profit = 0
        backward_profit_arr = [0] * len(prices)
        for i, p in reversed(list(enumerate(prices))):
            if sell < p:
                sell = p
                profit = 0
            else:
                profit = sell - p
            max_profit = profit if profit > max_profit else max_profit
            backward_profit_arr[i] = max_profit
        # find best split index
        max_profit = 0
        for i, profit in enumerate(forward_profit_arr):
            total_profit = profit
            if i < len(prices)-1:
                total_profit += backward_profit_arr[i+1]
            max_profit = total_profit if total_profit > max_profit else max_profit
        return max_profit
    # [0, 0, 4, 3, 0, 1]
    # [3, 4, 0, 0, 3, 0]
