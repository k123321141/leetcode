class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:  # noqa
        '''
        O(N^3), 68%
        '''
        S = set()
        for q1, q2 in equations:
            S.add(q1)
            S.add(q2)
        N = len(S)
        W = []
        idx_dict = {}
        for idx, q in enumerate(S):
            W.append([None]*N)
            idx_dict[q] = idx

        # init graph
        for (q1, q2), v in zip(equations, values):
            i, j = idx_dict[q1], idx_dict[q2]
            W[i][j] = v
            W[j][i] = 1. / v
            W[i][i] = 1
            W[j][j] = 1
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if W[i][k] and W[k][j]:
                        W[i][j] = W[i][k] * W[k][j]
        #
        ret = []
        for q1, q2 in queries:
            if q1 not in idx_dict or q2 not in idx_dict:
                result = -1
            else:
                i, j = idx_dict[q1], idx_dict[q2]
                if W[i][j]:
                    result = W[i][j]
                else:
                    result = -1
            ret.append(result)
        return ret
