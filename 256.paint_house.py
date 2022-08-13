class Solution:
    def minCost(self, costs: List[List[int]]) -> int:  # noqa
        '''
        O(3N)
        '''
        N = len(costs)
        for i in reversed(range(N-1)):
            # get 1st and 2nd minimum value
            min_1, min_2, v = costs[i+1]
            idx_1 = 0
            if min_2 < min_1:
                min_1, min_2 = min_2, min_1
                idx_1 = 1

            if v < min_1:
                min_2 = min_1
                min_1, idx_1 = v, 2
            elif v < min_2:
                min_2 = v
            #
            for j, c in enumerate(costs[i]):
                if j != idx_1:
                    costs[i][j] = c + min_1
                else:
                    costs[i][j] = c + min_2
        return min(costs[0])
