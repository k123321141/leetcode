from functools import cache


class Solution:
    def jump(self, nums: List[int]) -> int:  # noqa
        '''
        DP verison, O(N^2)

        '''
        self.nums = nums
        return self.dp(0)

    @cache
    def dp(self, idx: int):
        nums = self.nums
        if idx == (len(nums) - 1):
            return 0
        else:
            arr = [self.dp(idx + i) for i in range(1, nums[idx] + 1) if idx + i < len(nums)]
            if arr:
                return 1 + min(arr)
            else:
                return float('inf')
