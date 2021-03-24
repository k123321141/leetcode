class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:  # noqa
        '''
        Record max length and number of LIS for each index.
        O(N^2)
        13%
        '''
        if len(nums) == 1:
            return 1
        elif len(set(nums)) == 1:
            return len(nums)
        else:
            self.nums = nums
            leng_arr = [1] * len(nums)
            count_arr = [1] * len(nums)

            max_max_leng = 1
            max_count = 1
            for i in reversed(range(len(nums)-1)):
                max_leng = 1
                combination = 1
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        if leng_arr[j] + 1 > max_leng:
                            max_leng = leng_arr[j] + 1
                            combination = count_arr[j]
                        elif leng_arr[j] + 1 == max_leng:
                            combination += count_arr[j]
                leng_arr[i] = max_leng
                count_arr[i] = combination
                if max_leng > max_max_leng:
                    max_max_leng = max_leng
                    max_count = combination
                elif max_leng == max_max_leng:
                    max_count += combination
            return max_count
