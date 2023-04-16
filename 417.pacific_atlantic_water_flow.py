from collections import deque
from functools import lru_cache


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:  # noqa
        '''
        Run BFS for each corner to record wich cell can each the occean.
        O(2MN)
        '''
        self.heights = heights
        h = len(heights)
        w = len(heights[0])

        lu, rd = set(), set()

        # left up
        Q = deque()
        for y in range(h):
            Q.append((y, 0))
            lu.add((y, 0))
        for x in range(1, w):
            Q.append((0, x))
            lu.add((0, x))

        while Q:
            y, x = Q.popleft()
            for dst in self.adj(y, x):
                if dst not in lu:
                    lu.add(dst)
                    Q.append(dst)

        # right down
        ret = []
        Q = deque()
        for y in range(h):
            Q.append((y, w-1))
            rd.add((y, w-1))
        for x in range(w-1):
            Q.append((h-1, x))
            rd.add((h-1, x))

        while Q:
            src = y, x = Q.popleft()
            if src in lu:
                ret.append([y, x])
            for dst in self.adj(y, x):
                if dst not in rd:
                    rd.add(dst)
                    Q.append(dst)
        return ret

    @lru_cache
    def adj(self, y, x):
        heights = self.heights
        h = len(heights)
        w = len(heights[0])
        ret = []
        hei = heights[y][x]
        if x > 0 and hei <= heights[y][x-1]:
            ret.append((y, x-1))
        if x < w-1 and hei <= heights[y][x+1]:
            ret.append((y, x+1))
        if y > 0 and hei <= heights[y-1][x]:
            ret.append((y-1, x))
        if y < h-1 and hei <= heights[y+1][x]:
            ret.append((y+1, x))
        return ret
