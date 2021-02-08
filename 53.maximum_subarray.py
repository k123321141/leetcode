class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # noqa
        if len(nums) == 1:
            return nums[0]
        total = 0
        min_sum = float('inf')
        max_sum = float('-inf')
        for n in nums:
            total += n
            max_sum = max(max_sum, total-min(0, min_sum))
            if total < min_sum:
                min_sum = total
        return max_sum
