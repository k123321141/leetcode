class Solution:
    def minOperations(self, nums: List[int]) -> int:  # noqa
        counter = {}
        err = 0
        ret = 0
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
            if counter[n] == 1:
                err += 1
            elif counter[n] == 2:
                ret += 1
                err -= 1
            elif (counter[n] - 1) % 3 == 0:
                ret += 1
        if err:
            return -1
        return ret
