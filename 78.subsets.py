class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:  # noqa
        ret = [[], ]
        N = len(nums)
        for l in range(1, N + 1):
            self.traceback(ret, [], nums, 0, l)

        return ret

    def traceback(self, ret: list, prefix: list, nums: list, idx: int, target_len: int):
        if target_len == len(prefix):
            ret.append(prefix)
        else:
            # length check
            N = len(nums)
            for i in range(idx, N):
                if (N - i) >= (target_len - len(prefix)):
                    self.traceback(ret, prefix + [nums[i], ], nums, i + 1, target_len)
