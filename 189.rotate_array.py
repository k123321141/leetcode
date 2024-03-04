class Solution:
    def rotate(self, nums: List[int], k: int) -> None:  # noqa
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        k = k % L
        if k == 0:
            return

        factor = Solution.max_common_factor(L, k)
        if factor == 1:
            # if L is multiple of k, we can just swap the elements
            src = 0
            src_val = nums[src]
            for _ in range(L):
                dst = (src + k) % L
                # swap
                buf = nums[dst]
                nums[dst] = src_val
                src_val = buf
                src = dst
        else:
            for offset in range(factor):
                src = offset
                src_val = nums[src]
                for _ in range(L // factor):
                    dst = (src + k) % L
                    # swap
                    buf = nums[dst]
                    nums[dst] = src_val
                    src_val = buf
                    src = dst

            pass
        return

    @staticmethod
    def max_common_factor(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a
