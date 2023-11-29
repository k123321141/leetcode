import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:  # noqa
        '''O(KE)
        '''

        G = {i: [] for i in range(n)}
        for u, v, w in flights:
            G[u].append((v, w))

        if k <= 1:
            cost_dict = Solution.get_k_stops_cost(G, src, dst, k)
            min_cost = cost_dict.get(dst, -1)
            return min_cost if not math.isinf(min_cost) else -1

        inv_G = {i: [] for i in range(n)}
        for u, v, w in flights:
            inv_G[v].append((u, w))
        cost_dict = Solution.get_k_stops_cost(G, src, k // 2)
        inv_cost_dict = Solution.get_k_stops_cost(inv_G, src, int(math.ceil(k / 2) - 1))

        min_cost = float('inf')
        for mid, w1 in cost_dict.items():
            if mid in inv_cost_dict:
                w2 = inv_cost_dict[mid]
                min_cost = min(min_cost, w1 + w2)
        # return 99
        return min_cost if not math.isinf(min_cost) else -1

    def get_k_stops_cost(G, src, k) -> dict:
        pre_cost_dict = {}

        cost_dict = {src: 0}
        for v, w in G[src]:
            cost_dict[v] = w
        if k == 0:
            return cost_dict

        for _ in range(k):
            pre_cost_dict, cost_dict = cost_dict, pre_cost_dict
            for u in G:
                for v, w in G[u]:
                    cost_dict[v] = min(
                        cost_dict.get(v, float('inf')),
                        pre_cost_dict.get(u, float('inf')) + w,
                        pre_cost_dict.get(v, float('inf')),
                    )
        return cost_dict
