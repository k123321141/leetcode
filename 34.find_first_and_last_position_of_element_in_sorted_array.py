class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:  # noqa
        '''
        A variant of binary search.
        '''
        if len(nums) == 0:
            return [-1, -1]
        l = self.find_left(nums, target)
        r = self.find_right(nums, target)
        if l == -1 or r == -1 or l > r:
            return [-1, -1]
        else:
            return [l, r]

    def find_left(self, nums: List[int], target: int) -> List[int]:  # noqa
        l, r = 0, len(nums)-1
        if nums[l] == target:
            return l
        elif target < nums[l]:
            return -1

        while l < r:
            if r - l == 1:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1

            i = int((l+r)/2)
            if target <= nums[i]:
                r = i
            else:
                l = i

        return -1


    def find_right(self, nums: List[int], target: int) -> List[int]:  # noqa
        l, r = 0, len(nums)-1
        if nums[r] == target:
            return r
        elif nums[r] < target:
            return -1

        while l < r:
            if r - l == 1:
                if nums[r] == target:
                    return r
                elif nums[l] == target:
                    return l
                else:
                    return -1

            i = int((l+r)/2)
            if nums[i] <= target:
                l = i
            else:
                r = i

        return -1
