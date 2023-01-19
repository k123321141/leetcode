from functools import cache
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:  # noqa
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return max(0, nums[0])
        else:
            arr = sorted(set(nums))
            self.nums = arr
            self.counter = Counter(nums)
            print(arr)
            return max([self.dp(i) for i in range(len(arr))])

    @cache
    def dp(self, i):
        k = self.nums[i]
        v = k * self.counter[k]
        N = len(self.nums)
        if i+2 < N:
            if self.nums[i+1] == k+1:
                ret = max(v + self.dp(i+2), self.dp(i+1))
            else:
                ret = v + self.dp(i+1)

        elif i+1 < N:
            if self.nums[i+1] == k+1:
                ret = max(v, self.dp(i+1))
            else:
                ret = v + self.dp(i+1)
        else:
            ret = v
        return ret
