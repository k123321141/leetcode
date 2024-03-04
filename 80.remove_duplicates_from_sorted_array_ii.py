class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        count = {nums[0]: 1}

        for i in range(1, len(nums)):
            n = nums[i]
            c = count.get(n, 0)
            if c < 2:
                idx += 1
                nums[idx] = nums[i]
                count[n] = c + 1
            else:
                continue
        return idx + 1
