from functools import cache
from bisect import insort


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int: # noqa
        '''
        O(kN)
        Iterative searching cut-point for each interval.

        k = 4
        prices = [1,2,4,2,5,7,2,4,9,0]

        k = 2, [1,2,4,2,5,7], [2,4,9,0] <- search best cut-point for interval above.
        k = 3, [1,2,4], [2,5,7], [2,4,9,0]  <- search best cut-point for 2 intervals above.

        '''
        if k == 0 or len(prices) <= 1:
            return 0
        k = min(k, len(prices)//2)
        if k == 1:
            return Solution.one_direction(prices)
        else:
            self.prices = prices
            profit = Solution.one_direction(prices)
            max_increment, cut_point = self.get_increment(0, len(prices))
            if cut_point is None:
                return profit
            else:
                profit += max_increment
                cut_list = [cut_point, len(prices)]
                k -= 1
                while cut_point is not None and k > 1:
                    left = 0
                    max_increment = 0
                    for right in cut_list:
                        increment, cut = self.get_increment(left, right)
                        if increment > max_increment:
                            cut_point = cut
                            max_increment = increment

                        left = right
                    if cut_point is not None:
                        insort(cut_list, cut_point)
                        profit += max_increment

                    k -= 1
                return profit

    @staticmethod
    def one_direction(prices: List[int]) -> int: # noqa
        if len(prices) <= 1:
            return 0
        low = prices[0]
        profit = 0
        for p in prices[1:]:
            if p <= low:
                low = p
            else:
                diff = p - low
                profit = diff if diff > profit else profit

        return profit

    @cache
    def get_increment(self, left: int, right: int) -> int: # noqa
        '''
        1. Construct profit arrary for buy-first-sell-last process.
        2. Construct profit arrary for sell-first-buy-last process.
        3. Find the best profit in this 2 arrays.
        O(N)
        '''
        if right - left <= 1:
            return 0, None
        prices = self.prices
        # buy-first-sell-last
        buy = float('inf')
        max_profit = 0
        forward_profit_dict = {}
        for i in range(left, right):
            p = prices[i]
            if buy > p:
                buy = p
                profit = 0
            else:
                profit = p - buy
            max_profit = profit if profit > max_profit else max_profit
            forward_profit_dict[i] = max_profit
        # sell-first-buy-last
        sell = float('-inf')
        max_increment = 0
        cut_point = None
        for i in range(right-1, left, -1):
            p = prices[i]
            if sell < p:
                sell = p
                profit = 0
            else:
                profit = sell - p
            increment = (profit + forward_profit_dict[i-1]) - max_profit
            if increment > max_increment:
                max_increment = increment
                cut_point = i
        return max_increment, cut_point
