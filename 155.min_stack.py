from collections import deque


class MinStack:
    """
    maintain a dict to track min for given depth
    """

    def __init__(self):
        self.Q = deque()
        self.min_dict = {0: None}

    def push(self, val: int) -> None:
        pre_min = self.getMin()
        self.Q.append(val)

        if pre_min is None or val < pre_min:
            self.min_dict[len(self.Q)] = val
        else:
            self.min_dict[len(self.Q)] = pre_min

    def pop(self) -> None:
        return self.Q.pop()

    def top(self) -> int:
        if self.Q:
            return self.Q[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min_dict[len(self.Q)]
