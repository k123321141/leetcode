class Solution:
    def findMin(self, nums: List[int]) -> int:  # noqa
        if len(nums) == 1:
            return nums[0]
        pre = nums[0]
        for n in nums[1:]:
            if n < pre:
                return n
            else:
                pre = n
        return nums[0]
