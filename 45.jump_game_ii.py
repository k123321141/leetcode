class Solution:
    def jump(self, nums: List[int]) -> int:  # noqa
        '''
        reversed DP verison, O(N^2)

        '''
        self.nums = nums
        self.cache = {}
        return self.dp(len(nums) - 1)

    def dp(self, idx: int):
        nums = self.nums
        if idx == 0:
            return 0
        else:
            min_steps = float('inf')
            for i in range(0, idx):
                v = nums[i]
                k = i + v
                if k >= idx and k not in self.cache:
                    # valid jump
                    steps = 1 + self.dp(i)
                    if steps < min_steps:
                        min_steps = steps
            self.cache[idx] = min_steps
            return min_steps
