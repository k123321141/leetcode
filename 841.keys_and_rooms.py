from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:  # noqa
        '''
        Create a graph from rooms and run a BFS for it.
        O(N)
        '''
        Q = deque()
        Q.append(0)
        S = {0, }
        while Q:
            src = Q.popleft()
            for dst in rooms[src]:
                if dst not in S:
                    S.add(dst)
                    if len(S) == len(rooms):
                        return True
                    Q.append(dst)

        return False
