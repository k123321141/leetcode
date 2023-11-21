from collections import deque


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:  # noqa
        '''Run an BFS without visited O(Nk), OOM
        Try DFS
        '''
        k = k + 1
        if k <= 0:
            return -1
        G = {}
        inv_G = {}
        for u, v, w in flights:
            if u not in G:
                G[u] = []
            G[u].append((v, w))

            if v not in inv_G:
                inv_G[v] = []
            inv_G[v].append((u, w))

        if k % 2 == 0:
            src_path_dict = self.k_stops(G, src, k // 2)
        else:
            src_path_dict = self.k_stops(G, src, k // 2 + 1)

        dst_path_dict = self.k_stops(inv_G, dst, k // 2)
        min_cost = float('inf')
        for mid, src_cost in src_path_dict.items():
            if mid not in dst_path_dict:
                continue
            dst_cost = dst_path_dict[mid]
            cost = src_cost + dst_cost
            min_cost = min(min_cost, cost)
        return min_cost if min_cost != float('inf') else -1

    def k_stops(self, G, src, k):
        path_dict = {src: 0}
        if k == 0:
            return path_dict
        Q = deque()
        if src in G:
            for v, w in G[src]:
                Q.append((v, w, 1))
        while Q:
            u, cost, depth = Q.popleft()
            if path_dict.get(u, float('inf')) >= cost:
                path_dict[u] = cost
            if depth >= k:
                continue
            if u not in G:
                continue
            for v, w in G[u]:
                new_cost = cost + w
                Q.append((v, new_cost, depth + 1))
        return path_dict

    def dfs_k_stops(self, path_dict, G, src, k, depth):
        for v, w in G[src]:
            cost = path_dict[src] + w
            if path_dict.get(v, float('inf')) >= cost:
                path_dict[v] = cost
            if depth < k:
                self.dfs_k_stops(path_dict, G, v, k, depth + 1)

        path_dict = {src: 0}
        if k == 0:
            return path_dict
        if src in G:
            for v, w in G[src]:
                Q.append((v, w, 1))
        while Q:
            u, cost, depth = Q.popleft()
            if path_dict.get(u, float('inf')) >= cost:
                path_dict[u] = cost
            if depth >= k:
                continue
            if u not in G:
                continue
            for v, w in G[u]:
                new_cost = cost + w
                Q.append((v, new_cost, depth + 1))
        return path_dict

    def _dfs(self, G, src, k):
        path_dict = {src: 0}
        if k == 0:
            return path_dict
        Q = deque()
        if src in G:
            for v, w in G[src]:
                Q.append((v, w, 1))
        while Q:
            u, cost, depth = Q.popleft()
            if path_dict.get(u, float('inf')) >= cost:
                path_dict[u] = cost
            if depth >= k:
                continue
            if u not in G:
                continue
            for v, w in G[u]:
                new_cost = cost + w
                Q.append((v, new_cost, depth + 1))
        return path_dict
