class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:  # noqa
        if len(currentState) <= 1:
            return []
        ret = []
        for i in range(len(currentState) - 1):
            c = currentState[i]
            if c == '-':
                continue
            if self.is_sequence(currentState, i):
                ret.append(self.flip(currentState, i))
        return ret

    def is_sequence(self, currentState: str, index: int):
        c = currentState[index]
        next_c = currentState[index + 1]
        return c == next_c

    def flip(self, currentState: str, index: int) -> str:
        flip_s = '--'
        return currentState[:index] + flip_s + currentState[index + 2:]
