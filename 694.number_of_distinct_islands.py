from collections import deque


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:  # noqa
        '''
        Run BFS to find all the island and sort their coorinates as their signature
        '''
        h, w = len(grid), len(grid[0])

        visited = set()
        if h == 1 and w == 1:
            return 1 if grid[0][0] == 1 else 0
        elif h == 0 or w == 0:
            return 0

        Q = deque()
        ret = 0
        for y in range(len(grid)):
            for x, v in enumerate(grid[y]):
                if v == 1:
                    Q.append((x, y))
                    grid[y][x] = 2
                    island = self.BFS(grid, Q)
                    if island not in visited:
                        visited.add(island)
                        ret += 1
        return ret


    def BFS(self, grid: List[List[str]], Q: deque) -> tuple:  # noqa
        island = []
        while Q:
            x, y = Q.popleft()
            island.append((x, y))
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

        return self.normalize(island)

    def normalize(self, island: list) -> tuple:
        min_x, min_y = float('inf'), float('inf')
        for x, y in island:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
        ret = sorted([(x - min_x, y - min_y) for x, y in island])
        return tuple(ret)
