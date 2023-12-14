class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  # noqa
        '''
        Recording increasing sequence for both sides.
        time: O(N), space: O(N)
        '''

        if len(heights) == 0:
            return 0
        elif len(heights) == 0:
            return heights[0]
        N = len(heights)

        right_side_increase_len_arr = []
        left_side_increase_len_arr = []
        pre = heights[0]
        right_i = left_i = 0
        for j in range(1, N):
            h = heights[j]

            if pre > h:
                for idx in range(right_i, j):
                    right_side_increase_len_arr.append(j - idx)
                right_i = j
            if pre < h:
                for l in range(j-left_i):
                    left_side_increase_len_arr.append(l+1)
                left_i = j
            pre = h

        for idx in range(right_i, N):
            right_side_increase_len_arr.append(N - idx)

        for idx in reversed(range(left_i, N)):
            left_side_increase_len_arr.append(N - idx)

        print(right_side_increase_len_arr)
        print(left_side_increase_len_arr)
        max_area = float('-inf')
        min_h = float('inf')
        for i, h in enumerate(heights):
            area = h * (right_side_increase_len_arr[i] + left_side_increase_len_arr[i] - 1)

            max_area = max(max_area, area)
            min_h = min(min_h, h)
        return max(max_area, min_h * N)
