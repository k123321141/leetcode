class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.visited = set()
        return list(set(map(tuple, self.recursive_fn([], nums))))

    def recursive_fn(self, prefix: List[int], nums: List[int]) -> List[List[int]]:
        key = tuple(prefix)
        if key in self.visited:
            return []

        if len(nums) == 0:
            return [prefix, ]

        ret = []
        for i, n in enumerate(nums):
            if i == 0:
                rest = nums[1:]
            elif i == len(nums) - 1:
                rest = nums[:-1]
            else:
                rest = nums[:i] + nums[i+1:]
            next_prefix = prefix + [n]
            rest_ret = self.recursive_fn(next_prefix, rest)
            ret.extend(rest_ret)
        self.visited.add(key)
        return ret
