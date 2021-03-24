from functools import cache
from typing import Tuple, List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        '''
        Record max length and number of LIS for each index.
        O(N^2)
        13%
        '''
        if len(nums) == 1:
            return 1
        else:
            self.nums = nums
            result = [self.dp(i) for i in range(len(nums))]
            max_leng = max(result, key=lambda x: x[0])[0]
            combination = sum([count for leng, count in result if leng == max_leng])
            # for i in range(len(nums)):
                # print(f'index: {i}: {self.dp(i)}')
            # print(max_leng, combination)
            return combination

    @cache
    def dp(self, i: int) -> Tuple[int, int]:
        if i == len(self.nums) - 1:
            return 1, 1
        else:
            # find the max_leng
            max_leng = 1
            combination = 1
            for j in range(i+1, len(self.nums)):
                if self.nums[i] < self.nums[j]:
                    sub_leng, count = self.dp(j)
                    leng = 1 + sub_leng
                    if leng > max_leng:
                        combination = count
                        max_leng = leng
                    elif leng == max_leng:
                        combination += count
            return max_leng, combination
