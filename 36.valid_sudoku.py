class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  # noqa
        '''
        O(N)
        '''
        # memory
        memory = [False] * (9*(9+9+9))
        for y in range(9):
            for x in range(9):
                v = board[y][x]
                if v == '.':
                    continue
                v = int(v) - 1
                # row
                idx = 9*y + v
                if memory[idx]:
                    return False
                else:
                    memory[idx] = True
                # col
                idx = 81 + 9*x + v
                if memory[idx]:
                    return False
                else:
                    memory[idx] = True
                # cell
                idx = 162 + 9*(x//3 + 3*(y//3)) + v
                if memory[idx]:
                    return False
                else:
                    memory[idx] = True

        return True
