from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:  # noqa
        '''
        Run a BFS, complexity O(N^2) for adjacency matrix
        '''
        N = len(isConnected)
        if N == 0:
            return 0
        elif N == 1:
            return 1
        elif N == 2:
            return 1 if isConnected[0][1] == 1 or isConnected[1][0] == 1 else 2

        visited = set()
        Q = deque()
        ret = 0
        for i in range(N):
            if i not in visited:
                Q.append(i)
                Solution.BFS(Q, visited, isConnected)
                ret += 1
        return ret

    @staticmethod
    def BFS(Q, visited, isConnected):
        while Q:
            i = Q.popleft()
            visited.add(i)
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    Q.append(j)
