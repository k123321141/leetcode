class Solution:
    def rob(self, nums: List[int]) -> int: # noqa
        '''
        iterative version 86%
        Keep tracking index that can make max sum for nums[idx:] array.

        '''
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            nums[-2] = nums[-1] if nums[-1] > nums[-2] else nums[-2]

            for i in range(len(nums)-3, -1, -1):
                nums[i] = max(nums[i] + nums[i+2], nums[i+1])
            return nums[0]
