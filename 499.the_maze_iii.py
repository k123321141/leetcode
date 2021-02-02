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
        if s == 0:
            return False
        else:
            return True

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:  # noqa
        '''
        Run a A* algorithm with manhattan distance heuristic.
        '''
        Q = []

        # dst reachable check 100%
        if not Solution.dst_check(maze, hole):
            return 'impossible'

        h, w = len(maze), len(maze[0])

        Q = []
        visited = set()

        y, x = ball
        p = (y, x)
        hole = tuple(hole)

        heapq.heappush(Q, (0, '', 0, y, x))
        visited.add(p)

        # print maze
        '''
        x = [[v for v in r] for r in maze]
        x[ball[0]][ball[1]] = 'x'
        x[hole[0]][hole[1]] = 'y'
        for row in x:
            print(str(row).replace(',', '').replace("'", ""))
        '''

        # skip-set skip those node that with better priority
        default_tuple = (float('inf'), '')
        Q_priority_dict = {p: default_tuple}

        while Q:
            src = heapq.heappop(Q)
            priority, prefix, cost, y, x = src
            # print(src)
            t = (priority, prefix)

            # skip-set skip those node that with better priority
            p = (y, x)
            if Q_priority_dict.get(p, default_tuple) < t:
                continue
            # left
            if x > 0 and maze[y][x-1] != 1:
                next_prefix = f'{prefix}l'
                x -= 1
                while x >= 0 and maze[y][x] == 0:
                    if y == hole[0] and x == hole[1]:
                        x -= 1
                        break
                    x -= 1
                p = (y, x+1)
                dis = abs(src[3]-p[0]) + abs(src[4]-p[1])
                if p == hole:
                    return next_prefix
                else:
                    manhattan_dis = abs(hole[0]-p[0]) + abs(hole[1]-p[1])
                    gn = manhattan_dis + cost + dis

                    if p not in visited or (gn, next_prefix) < Q_priority_dict[p]:
                        heapq.heappush(Q, (gn, next_prefix, cost+dis, p[0], p[1]))
                        # update key
                        Q_priority_dict[p] = (gn, next_prefix)
                        visited.add(p)

            # right
            priority, prefix, cost, y, x = src
            if x < w-1 and maze[y][x+1] != 1:
                next_prefix = f'{prefix}r'
                x += 1
                while x < w and maze[y][x] == 0:
                    if y == hole[0] and x == hole[1]:
                        x += 1
                        break
                    x += 1
                p = (y, x-1)
                dis = abs(src[3]-p[0]) + abs(src[4]-p[1])
                if p == hole:
                    return next_prefix
                else:
                    manhattan_dis = abs(hole[0]-p[0]) + abs(hole[1]-p[1])
                    gn = manhattan_dis + cost + dis

                    if p not in visited or (gn, next_prefix) < Q_priority_dict[p]:
                        heapq.heappush(Q, (gn, next_prefix, cost+dis, p[0], p[1]))
                        # update key
                        Q_priority_dict[p] = (gn, next_prefix)
                        visited.add(p)

            # up
            priority, prefix, cost, y, x = src
            if y > 0 and maze[y-1][x] != 1:
                next_prefix = f'{prefix}u'
                y -= 1
                while y >= 0 and maze[y][x] == 0:
                    if y == hole[0] and x == hole[1]:
                        y -= 1
                        break
                    y -= 1
                p = (y+1, x)
                dis = abs(src[3]-p[0]) + abs(src[4]-p[1])
                if p == hole:
                    return next_prefix
                else:
                    manhattan_dis = abs(hole[0]-p[0]) + abs(hole[1]-p[1])
                    gn = manhattan_dis + cost + dis

                    if p not in visited or (gn, next_prefix) < Q_priority_dict[p]:
                        heapq.heappush(Q, (gn, next_prefix, cost+dis, p[0], p[1]))
                        # update key
                        Q_priority_dict[p] = (gn, next_prefix)
                        visited.add(p)

            # down
            priority, prefix, cost, y, x = src
            if y < h-1 and maze[y+1][x] != 1:
                next_prefix = f'{prefix}d'
                y += 1
                while y < h and maze[y][x] == 0:
                    if y == hole[0] and x == hole[1]:
                        y += 1
                        break
                    y += 1
                p = (y-1, x)
                dis = abs(src[3]-p[0]) + abs(src[4]-p[1])
                if p == hole:
                    return next_prefix
                else:
                    manhattan_dis = abs(hole[0]-p[0]) + abs(hole[1]-p[1])
                    gn = manhattan_dis + cost + dis

                    if p not in visited or (gn, next_prefix) < Q_priority_dict[p]:
                        print('a')
                        heapq.heappush(Q, (gn, next_prefix, cost+dis, p[0], p[1]))
                        # update key
                        Q_priority_dict[p] = (gn, next_prefix)
                        visited.add(p)

        return 'impossible'
