class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # noqa
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # shift nums1
        for i in reversed(range(m)):
            nums1[n + i] = nums1[i]
        # insertion sort, maintain 2 index
        idx1 = 0
        idx2 = 0
        idx = 0
        while idx1 < m and idx2 < n:
            if nums1[n + idx1] <= nums2[idx2]:
                nums1[idx] = nums1[n + idx1]
                idx1 += 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 += 1
            idx += 1
        if idx2 < n:
            for i in range(idx2, n):
                nums1[m + i] = nums2[i]
