from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:  # noqa
        """
        Run BFS for each Os whether it is adjacent to boarder.
        O(N)
        """
        h = len(board)
        w = len(board[0])
        if h == 1 or w == 1:
            return

        self.visited = set()
        self.board = board

        # check the boarder
        for y in [0, h - 1]:
            row = board[y]
            for x, v in enumerate(row):
                if v == 'O' and (x, y) not in self.visited:
                    self.visited.add((x, y))
                    self.bfs(x, y)
        for x in [0, w - 1]:
            for y in range(h):
                v = board[y][x]
                if v == 'O' and (x, y) not in self.visited:
                    self.visited.add((x, y))
                    self.bfs(x, y)

        # flip all Os which not in visited
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                v = board[y][x]
                if v == 'O' and (x, y) not in self.visited:
                    board[y][x] = 'X'

    def bfs(self, x: int, y: int):

        h = len(self.board)
        w = len(self.board[0])

        Q = deque()
        Q.append((x, y))
        while Q:
            x, y = Q.popleft()

            if y+1 < h and self.board[y+1][x] == 'O' and (x, y+1) not in self.visited:
                Q.append((x, y+1))
                self.visited.add((x, y+1))
            if x+1 < w and self.board[y][x+1] == 'O' and (x+1, y) not in self.visited:
                Q.append((x+1, y))
                self.visited.add((x+1, y))
            if y > 0 and self.board[y-1][x] == 'O' and (x, y-1) not in self.visited:
                Q.append((x, y-1))
                self.visited.add((x, y-1))
            if x > 0 and self.board[y][x-1] == 'O' and (x-1, y) not in self.visited:
                Q.append((x-1, y))
                self.visited.add((x-1, y))
