from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:  # noqa
        '''
        O(N), 2 represents visited
        '''
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0

        Q = deque()
        max_area = 0
        for y in range(len(grid)):
            for x, v in enumerate(grid[y]):
                if v == 1:
                    Q.append((x, y))
                    grid[y][x] = 2
                    area = self.BFS(grid, Q)
                    max_area = max(area, max_area)
        return max_area

    def BFS(self, grid: List[List[int]], Q: deque) -> int:  # noqa
        area = 0
        while Q:
            area += 1
            x, y = Q.popleft()
            # up
            if y > 0 and grid[y-1][x] == 1:
                grid[y-1][x] = 2
                Q.append((x, y-1))
            # down
            if y < len(grid)-1 and grid[y+1][x] == 1:
                grid[y+1][x] = 2
                Q.append((x, y+1))
            # left
            if x > 0 and grid[y][x-1] == 1:
                grid[y][x-1] = 2
                Q.append((x-1, y))
            # right
            if x < len(grid[0])-1 and grid[y][x+1] == 1:
                grid[y][x+1] = 2
                Q.append((x+1, y))
        return area
