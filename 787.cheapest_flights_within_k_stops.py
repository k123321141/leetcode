

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:  # noqa
        '''O(KE)
        '''

        G = {i: [] for i in range(n)}

        for u, v, w in flights:
            G[u].append((v, w))
        cost_dict = {(src, i): 0 for i in range(k + 1)}
        for v, w in G[src]:
            cost_dict[(v, 0)] = w
        if k == 0:
            return cost_dict.get((dst, 0), -1)

        for i in range(1, k + 1):
            # print(cost_dict)
            for u, v, w in flights:
                if (u, i - 1) in cost_dict:
                    if (v, i) in cost_dict:
                        cost_dict[(v, i)] = min(cost_dict[(v, i)], cost_dict[(u, i - 1)] + w)
                    elif (v, i - 1) not in cost_dict:
                        cost_dict[(v, i)] = cost_dict[(u, i - 1)] + w
                    else:
                        # print('------------')
                        # print((v, i), ' = ', cost_dict[(v, i - 1)])
                        # print((v, i), ' = ', cost_dict[(u, i - 1)] + w)
                        cost_dict[(v, i)] = min(cost_dict[(v, i - 1)], cost_dict[(u, i - 1)] + w)
        # print(cost_dict)
        if (dst, k) in cost_dict:
            return cost_dict[(dst, k)]
        else:
            return -1
