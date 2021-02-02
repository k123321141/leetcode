class Solution:
    def countBattleships(self, board: List[List[str]]) -> int: # noqa
        if len(board) == 0:
            return 0
        h, w = len(board), len(board[0])
        count = 0
        if h == 1:
            pre = "."
            for i in range(w):
                v = board[0][i]
                if pre == "." and v == "X":
                    count += 1
                    pre = "X"
                elif pre == "X" and v == "X":
                    continue
                elif pre == "X" and v == ".":
                    pre = "."
                # elif pre == "." and V == ".":
                else:
                    continue
            return count
        elif w == 1:
            pre = "."
            for i in range(h):
                v = board[i][0]
                if pre == "." and v == "X":
                    pre = "X"
                    count += 1
                elif pre == "X" and v == "X":
                    continue
                elif pre == "X" and v == ".":
                    pre = "."
                # elif pre == "." and V == ".":
                else:
                    continue
            return count

        # for row in board:
            # print(' '.join(row))
        for y, row in enumerate(board):
            for x, v in enumerate(row):
                if v == "X":
                    # horizontal start
                    if (x == 0 or board[y][x-1] == ".") and (y == 0 or board[y-1][x] == ".") and (y == h-1 or board[y+1][x] == "."):
                        # print(f'dor or hor: ({x}, {y})')
                        count += 1
                    # vertical start
                    elif (x == 0 or board[y][x-1] == ".") and (x == w-1 or board[y][x+1] == ".") and (y == 0 or board[y-1][x] == "."):
                        # print(f'ver: ({x}, {y})')
                        count += 1

        return count
