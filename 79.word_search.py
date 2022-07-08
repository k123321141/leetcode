from collections import deque
from itertools import chain


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:  # noqa
        """
        Run DFS for each start node.
        Complexity: O(N^2 * N^2)
        """
        if not self.check_char_exist(board, word):
            return False

        h, w = len(board), len(board[0])
        start_char = word[0]
        for y in range(h):
            for x in range(w):
                if start_char == board[y][x] and self.bfs(board, word, (y, x)):
                    return True
        return False

    def check_char_exist(self, board, word):
        word_set = set(chain(*board))
        for w in word:
            if w not in word_set:
                return False
        return True

    def bfs(self, board: List[List[str]], word: str, start: tuple) -> bool:  # noqa
        h, w = len(board), len(board[0])
        path = [start, ]
        Q = deque([path, ])
        while Q:
            path = Q.pop()
            idx = len(path)
            node = path[-1]

            if idx == len(word):
                return True

            # search next char
            next_char = word[idx]
            y, x = node

            # 4 directions
            if y > 0 and board[y-1][x] == next_char:
                next_node = (y-1, x)
                if next_node not in path:
                    Q.append(path + [next_node])

            if y+1 < h and board[y+1][x] == next_char:
                next_node = (y+1, x)
                if next_node not in path:
                    Q.append(path + [next_node])

            if x > 0 and board[y][x-1] == next_char:
                next_node = (y, x-1)
                if next_node not in path:
                    Q.append(path + [next_node])
            if x+1 < w and board[y][x+1] == next_char:
                next_node = (y, x+1)
                if next_node not in path:
                    Q.append(path + [next_node])

        return False
