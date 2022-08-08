from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        DP recusive. 97%
        '''
        count_dict = defaultdict(int)
        for c in candidates:
            count_dict[c] += 1
        self.candidates = [(k, count_dict[k]) for k in sorted(count_dict.keys())]
        ret = self.dp(0, target)
        return ret

    @lru_cache
    def dp(self, idx: int, target: int) -> list:
        candidates = self.candidates
        ret = []
        for i in range(idx, len(candidates)):
            k, count = candidates[i]
            if k > target:
                break
            for c in range(count):
                v = k * (c + 1)
                if v < target and i + 1 < len(candidates):
                    tmp = [k] * (c + 1)
                    for rest_arr in self.dp(i + 1, target - v):
                        ret.append(tmp + rest_arr)
                elif v == target:
                    ret.append([k] * (c + 1))
        return ret
