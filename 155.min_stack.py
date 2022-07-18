from collections import deque


class MinStack:

    def __init__(self):
        self.Q = deque()
        self.min = None

    def push(self, val: int) -> None:
        pre_min = self.getMin()
        if pre_min is None or val < pre_min:
            self.min = val
        element = (val, pre_min)
        self.Q.append(element)

    def pop(self) -> None:
        val, pre_min = self.Q.pop()
        self.min = pre_min
        return val

    def top(self) -> int:
        if self.Q:
            return self.Q[-1][0]
        else:
            return None

    def getMin(self) -> int:
        return self.min
