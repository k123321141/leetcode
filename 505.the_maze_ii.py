import heapq


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

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:  # noqa
        '''
        Run a A* algorithm with manhattan distance heuristic.
        '''
        Q = []

        # dst reachable check 100%
        if not Solution.dst_check(maze, destination):
            return -1
        #

        h, w = len(maze), len(maze[0])

        Q = []
        visited = set()

        y, x = start
        p = (y, x)
        destination = tuple(destination)

        heapq.heappush(Q, (0, 0, y, x))
        visited.add(p)
        
        # skip-set skip those node that with better priority
        Q_priority_dict = {p: 0}

        while Q:
            src = heapq.heappop(Q)
            # left
            priority, cost, y, x = src

            # skip-set skip those node that with better priority
            p = (y, x)
            if Q_priority_dict.get(p, float('inf')) < priority:
                continue
            if x > 0 and maze[y][x-1] != 1:
                x -= 1
                while x >= 0 and maze[y][x] == 0:
                    x -= 1
                p = (y, x+1)
                dis = abs(src[2]-p[0]) + abs(src[3]-p[1])
                if p == destination:
                    return cost + dis

                manhattan_dis = abs(destination[0]-p[0]) + abs(destination[1]-p[1])
                gn = manhattan_dis + cost + dis

                if p not in visited or gn < Q_priority_dict[p]:
                    heapq.heappush(Q, (gn, cost+dis, p[0], p[1]))
                    # update key
                    Q_priority_dict[p] = gn
                    visited.add(p)

            # right
            _, cost, y, x = src
            if x < w-1 and maze[y][x+1] != 1:
                x += 1
                while x < w and maze[y][x] == 0:
                    x += 1
                p = (y, x-1)
                dis = abs(src[2]-p[0]) + abs(src[3]-p[1])
                if p == destination:
                    return cost + dis

                manhattan_dis = abs(destination[0]-p[0]) + abs(destination[1]-p[1])
                gn = manhattan_dis + cost + dis

                if p not in visited or gn < Q_priority_dict[p]:
                    heapq.heappush(Q, (gn, cost+dis, p[0], p[1]))
                    # update key
                    Q_priority_dict[p] = gn
                    visited.add(p)
            # up
            _, cost, y, x = src
            if y > 0 and maze[y-1][x] != 1:
                y -= 1
                while y >= 0 and maze[y][x] == 0:
                    y -= 1
                p = (y+1, x)
                dis = abs(src[2]-p[0]) + abs(src[3]-p[1])
                if p == destination:
                    return cost + dis

                manhattan_dis = abs(destination[0]-p[0]) + abs(destination[1]-p[1])
                gn = manhattan_dis + cost + dis

                if p not in visited or gn < Q_priority_dict[p]:
                    heapq.heappush(Q, (gn, cost+dis, p[0], p[1]))
                    # update key
                    Q_priority_dict[p] = gn
                    visited.add(p)
            # down
            _, cost, y, x = src
            if y < h-1 and maze[y+1][x] != 1:
                y += 1
                while y < h and maze[y][x] == 0:
                    y += 1
                p = (y-1, x)
                dis = abs(src[2]-p[0]) + abs(src[3]-p[1])
                if p == destination:
                    return cost + dis

                manhattan_dis = abs(destination[0]-p[0]) + abs(destination[1]-p[1])
                gn = manhattan_dis + cost + dis

                if p not in visited or gn < Q_priority_dict[p]:
                    heapq.heappush(Q, (gn, cost+dis, p[0], p[1]))
                    # update key
                    Q_priority_dict[p] = gn
                    visited.add(p)
        return -1
