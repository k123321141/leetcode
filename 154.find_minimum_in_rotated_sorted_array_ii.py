class Solution:
    def findMin(self, nums: List[int]) -> int:  # noqa
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        while nums[l] >= nums[r]:  # not sorted array
            idx = (l+r)//2
            if idx == l:
                return min(nums[l], nums[r])
            else:
                if nums[idx] >= nums[l]:
                    l = idx
                else:
                    r = idx
        return min(nums[l], nums[r])
