from typing import List
from functools import lru_cache


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: # noqa
        '''
        DP recusive. 97%
        '''
        candidates = sorted(candidates)
        self.candidates = candidates
        return self.dp(0, target)

    @lru_cache
    def dp(self, idx: int, target: int) -> list:
        candidates = self.candidates
        ret = []
        for i in range(idx, len(candidates)):
            v = candidates[i]
            if v < target:
                tmp = [v, ]
                for rest_arr in self.dp(i, target - v):
                    ret.append(tmp + rest_arr)
            elif v == target:
                ret.append([v, ])
        return ret
