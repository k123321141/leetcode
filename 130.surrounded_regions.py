from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:  # noqa
        """
        Run BFS for each Os whether it is adjacent to boarder.
        """

        self.visited = set()
        self.board = board
        for y, row in enumerate(board):
            for x, v in enumerate(row):
                if v == 'O' and (x, y) not in self.visited:
                    self.bfs(x, y)

    def bfs(self, x: int, y: int):

        h = len(self.board)
        w = len(self.board[0])

        path = []
        Q = deque()
        Q.append((x, y))
        boarder_flag = False
        while Q:
            node = x, y = Q.popleft()
            self.visited.add(node)
            path.append(node)
            if (y+1) == h or y == 0 or (x+1) == w or x == 0:
                boarder_flag = True

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
        if not boarder_flag:
            for x, y in path:
                self.board[y][x] = 'X'
    # [["O","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","X","O","X","O","O","O","O","X","O","O","X","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","X","O"],["O","X","X","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","O","O","X","O","O","O","O","O","X","X","O"],["O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","X","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","O","O","O","O","X","X","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O"],["O","O","O","O","X","O","O","O","O","O","O","O","O","X","O","O","O","O","O","X"],["O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","X","O","X","O","O"],["O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","X","X","O","O","O","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"]]
