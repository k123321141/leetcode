from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # noqa
        '''
        Run multiple BFS to search all islands.
        '''

        h, w = len(grid), len(grid[0])

        if h == 1 and w == 1:
            return 1 if grid[0][0] == "1" else 0
        elif h == 0 or w == 0:
            return 0

        Q = deque()
        ret = 0
        for y in range(len(grid)):
            for x, v in enumerate(grid[y]):
                if v == "1":
                    ret += 1
                    Q.append((x, y))
                    grid[y][x] = 2
                    self.BFS(grid, Q)
                    print(x, y, grid)
        return ret

    def BFS(self, grid: List[List[str]], Q: deque):  # noqa
        while Q:
            x, y = Q.popleft()
            # up
            if y > 0 and grid[y-1][x] == "1":
                grid[y-1][x] = 2
                Q.append((x, y-1))
            # down
            if y < len(grid)-1 and grid[y+1][x] == "1":
                grid[y+1][x] = 2
                Q.append((x, y+1))
            # left
            if x > 0 and grid[y][x-1] == "1":
                grid[y][x-1] = 2
                Q.append((x-1, y))
            # right
            if x < len(grid[0])-1 and grid[y][x+1] == "1":
                grid[y][x+1] = 2
                Q.append((x+1, y))
