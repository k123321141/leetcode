from functools import cache


class Solution:

    @cache
    def canWin(self, currentState: str) -> bool:
        if len(currentState) <= 1:
            return False

        for i in range(len(currentState) - 1):
            c = currentState[i]
            if c == '-':
                continue
            if self.is_sequence(currentState, i):
                next_state = self.flip(currentState, i)
                if not self.canWin(next_state):
                    return True
        return False

    def is_sequence(self, currentState: str, index: int):
        c = currentState[index]
        next_c = currentState[index + 1]
        return c == next_c

    def flip(self, currentState: str, index: int) -> str:
        flip_s = '--'
        return currentState[:index] + flip_s + currentState[index + 2:]
