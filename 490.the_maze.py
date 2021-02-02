from collections import deque


class Solution:
    @staticmethod
    def dst_check(maze: List[List[int]], destination: List[int]) -> bool:  # noqa
        h, w = len(maze), len(maze[0])
        y, x = destination
        l = x != 0 and maze[y][x-1] == 0
        r = x != w-1 and maze[y][x+1] == 0
        u = y != 0 and maze[y-1][x] == 0
        d = y != h-1 and maze[y+1][x] == 0

        s = l+r+u+d
        if s == 4:
            return False
        elif s == 1 or s == 3:
            return True
        elif s == 2:
            if l and r:
                return False
            elif u and d:
                return False
            else:
                return True
        else:
            return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:  # noqa
        '''
        Run a BFS to search solution
        '''
        # start from start point 66%

        # dst reachable check 100%
        if not Solution.dst_check(maze, destination):
            return False
        #

        h, w = len(maze), len(maze[0])

        Q = deque()
        visited = set()

        y, x = start
        p = (y, x)
        destination = tuple(destination)

        Q.append(p)
        visited.add(p)

        while Q:
            src = Q.popleft()
            # left
            y, x = src
            if x > 0 and maze[y][x-1] != 1:
                x -= 1
                while x >= 0 and maze[y][x] == 0:
                    x -= 1
                p = (y, x+1)
                if p == destination:
                    return True
                if p not in visited:
                    Q.append(p)
                    visited.add(p)
            # right
            y, x = src
            if x < w-1 and maze[y][x+1] != 1:
                x += 1
                while x < w and maze[y][x] == 0:
                    x += 1
                p = (y, x-1)
                if p == destination:
                    return True
                if p not in visited:
                    Q.append(p)
                    visited.add(p)
            # up
            y, x = src
            if y > 0 and maze[y-1][x] != 1:
                y -= 1
                while y >= 0 and maze[y][x] == 0:
                    y -= 1
                p = (y+1, x)
                if p == destination:
                    return True
                if p not in visited:
                    Q.append(p)
                    visited.add(p)
            # down
            y, x = src
            if y < h-1 and maze[y+1][x] != 1:
                y += 1
                while y < h and maze[y][x] == 0:
                    y += 1
                p = (y-1, x)
                if p == destination:
                    return True
                if p not in visited:
                    Q.append(p)
                    visited.add(p)
        return False
