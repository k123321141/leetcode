from collections import deque


class CustomList(list):
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return id(self) == id(other)


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:  # noqa
        '''
        Run a BFS to record each island size, iterative visit each 0 to sum largest island size.
        2-pass O(N^2)
        space O(N^2)
        '''
        hashdict = {}

        Q = deque()
        for y in range(len(grid)):
            for x, v in enumerate(grid[y]):
                if v == 1:
                    Q.append((x, y))
                    grid[y][x] = 2
                    island = self.BFS(grid, Q)
                    for point in island:
                        hashdict[point] = island

        ret = 0
        all_land = True
        for y in range(len(grid)):
            for x, v in enumerate(grid[y]):
                if v == 1:
                    continue
                all_land = False
                ret = max(ret, self.get_area(grid, hashdict, (y, x)))
        print(f'all_land: {all_land}')
        if all_land:
            return len(grid) * len(grid[0])
        return ret

    def BFS(self, grid: List[List[str]], Q: deque) -> CustomList:  # noqa
        island = CustomList()

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

        return island

    def get_area(self, grid: List[List[str]], hashdict: dict, point: tuple) -> int:  # noqa
        y, x = point
        list_of_island = set()
        # up
        if (y-1, x) in hashdict:
            list_of_island.add(hashdict[(y-1, x)])
        # down
        if (y+1, x) in hashdict:
            list_of_island.add(hashdict[(y+1, x)])
        # left
        if (y, x-1) in hashdict:
            list_of_island.add(hashdict[(y, x-1)])
        # right
        if (y, x+1) in hashdict:
            list_of_island.add(hashdict[(y, x+1)])
        ret = sum([len(island) for island in list_of_island]) + 1
        return ret
