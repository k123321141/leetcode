from typing import List
from functools import lru_cache


class Solution:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.limit = {}
        for i in range(1, 10):
            if i == 1:
                self.limit[i] = 10 - i
            else:
                self.limit[i] = 10 - i + self.limit[i-1]

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.candidates = list(range(1, 10))
        return self.dp(0, k, n)

    @lru_cache
    def dp(self, idx: int, k: int, target: int) -> list:
        if target > self.limit[k]:
            return []
        elif target == self.limit[k]:
            return [list(range(10 - k, 10)), ]

        candidates = self.candidates
        ret = []
        for i in range(idx, len(candidates)):
            v = candidates[i]
            if v > target:
                break
            if v < target and i + 1 < len(candidates) and k > 1 and target - v <= self.limit[k-1] and target - v >= i + 1:
                tmp = [v, ]
                for rest_arr in self.dp(i + 1, k - 1, target - v):
                    ret.append(tmp + rest_arr)
            elif v == target and k == 1:
                ret.append([v, ])
                break
        return ret
