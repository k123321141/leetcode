class Solution:
    def singleNumber(self, nums: List[int]) -> int:  # noqa
        x = 0
        for n in nums:
            x ^= n
        return x
