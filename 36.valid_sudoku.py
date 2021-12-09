class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  # noqa
        # row
        for y in range(9):
            visited = [False]*9
            for x in range(9):
                v = board[y][x]
                if v == '.':
                    continue
                v = int(v) - 1
                if visited[v]:
                    return False
                else:
                    visited[v] = True
        # col
        for x in range(9):
            visited = [False]*9
            for y in range(9):
                v = board[y][x]
                if v == '.':
                    continue
                v = int(v) - 1
                if visited[v]:
                    return False
                else:
                    visited[v] = True
        # cell
        for offset_x in range(3):
            for offset_y in range(3):
                visited = [False]*9
                for x in range(3):
                    for y in range(3):
                        v = board[y+offset_y*3][x+offset_x*3]
                        if v == '.':
                            continue
                        v = int(v) - 1
                        if visited[v]:
                            return False
                        else:
                            visited[v] = True
        return True
