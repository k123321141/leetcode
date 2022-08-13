class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:  # noqa
        '''
        O(kN)
        '''
        N = len(costs)
        for i in reversed(range(N-1)):
            # get 1st and 2nd minimum value
            min_1, min_2 = costs[i+1][:2]
            idx_1 = 0
            if min_2 < min_1:
                min_1, min_2 = min_2, min_1
                idx_1 = 1
            for j in range(2, len(costs[i+1])):
                v = costs[i+1][j]
                if v < min_1:
                    min_2 = min_1
                    min_1, idx_1 = v, j
                elif v < min_2:
                    min_2 = v
            #
            for j, c in enumerate(costs[i]):
                costs[i][j] = c + min_1 if j != idx_1 else c + min_2
        return min(costs[0])
