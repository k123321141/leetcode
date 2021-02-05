from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int: # noqa
        '''
        DP vresion 25%
        Keep tracking index that can make max sum for nums[idx:] array.

        '''
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            self.nums = nums
            return max([self.dp(i) for i in range(len(nums))])

    @lru_cache
    def dp(self, idx: int):
        if idx == len(self.nums) - 1:
            ret = max(0, self.nums[idx])
        elif idx == len(self.nums) - 2:
            ret = max(0, self.nums[idx], self.nums[idx+1])
        else:
            ret = max(0, *[self.nums[idx] + self.dp(i) for i in range(idx+2, len(self.nums))])
        # print(f'idx: {idx}, ret: {ret}')
        return ret
