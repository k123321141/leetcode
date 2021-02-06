from typing import List


class Node:
    def __init__(self, s: str):
        self.s = s
        self.neighbors = []


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join([str(i) for i in range(k)])
        elif k == 1:
            return '0'*n
        
        S = []
        self.get_permutation(n, k, '', S)

        V = {}
        for s in S:
            if s not in V:
                V[s] = Node(s)
            node = V[s]
            for sub_s in S:
                if s == sub_s:
                    continue
                if sub_s.startswith(s[-(n-1):]):
                    if sub_s not in V:
                        V[sub_s] = Node(sub_s)
                    node.neighbors.append(V[sub_s])
        # greedy
        visited = set()
        ret = ''
        node = V[s]
        path = []
        while len(visited) < len(V):
            x = None
            for dst in node.neighbors:
                if dst.s not in visited:
                    node = x = dst
                    break
            assert x is not None
            visited.add(node.s)
            path.append(node.s)
        ret = path[0] + ''.join([s[-1]for s in path[1:]])
        return ret

    def get_permutation(self, n: int, k: int, prefix: str, ret: List[str]):
        if len(prefix) == n:
            ret.append(prefix)
        else:
            for i in range(k):
                self.get_permutation(n, k, prefix+str(i), ret)
