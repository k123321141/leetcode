from collections import deque


class Solution:

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:  # noqa
        '''
        O(N), 2 represents visited
        space O(N)
        '''
        if len(grid2) == 0:
            return 0
        if len(grid2[0]) == 0:
            return 0

        Q = deque()
        count = 0
        for y in range(len(grid2)):
            for x, v in enumerate(grid2[y]):
                if v == 1 and grid1[y][x] == 1:
                    grid2[y][x] = 2
                    Q.append((x, y))
                    if self.BFS(grid1, grid2, Q):
                        count += 1

        return count

    def BFS(self, grid1: List[List[int]], grid2: List[List[int]], Q: deque) -> bool:  # noqa
        ret = True
        while Q:
            x, y = Q.popleft()
            if grid1[y][x] == 0:
                ret = False
            # up
            if y > 0 and grid2[y-1][x] == 1:
                grid2[y-1][x] = 2
                Q.append((x, y-1))
            # down
            if y < len(grid2)-1 and grid2[y+1][x] == 1:
                grid2[y+1][x] = 2
                Q.append((x, y+1))
            # left
            if x > 0 and grid2[y][x-1] == 1:
                grid2[y][x-1] = 2
                Q.append((x-1, y))
            # right
            if x < len(grid2[0])-1 and grid2[y][x+1] == 1:
                grid2[y][x+1] = 2
                Q.append((x+1, y))
        return ret
