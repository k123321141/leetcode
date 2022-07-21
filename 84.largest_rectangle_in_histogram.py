class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  # noqa
        '''
        Maintain a dict which record minimum height for given range (a, b).
        O(N^2)
        '''
        low_dict = {}
        N = len(heights)
        for i in range(N):
            low = heights[i]
            low_dict[(i, i+1)] = low
            for j in range(i+1, N):
                low = min(low, heights[j])
                low_dict[(i, j+1)] = low

        for j in range(N-1, 1, -1):
            low = heights[j-1]
            low_dict[(j-1, j)] = low
            for i in range(j-1, 0, -1):
                low = min(low, heights[i])
                low_dict[(i, j)] = low
        max_area = float('-inf')
        for i in range(N):
            for j in range(i+1, N+1):
                area = (j - i) * low_dict[(i, j)]
                max_area = max(max_area, area)
        return max_area
