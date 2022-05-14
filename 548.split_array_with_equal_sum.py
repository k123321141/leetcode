class Solution:
    '''
    題目為 數列中 刪除三個不相連子數列 剩餘四個子數列後總和相同
    從左邊開始加總 會得到所有可能的總和數字
    從右邊亦然 所以總和數字必定是交集
    然後從中間剩餘的數列找符合的子數列
    '''
    def splitArray(self, nums: List[int]) -> bool:  # noqa
        if len(nums) < 7:
            return False
        N = len(nums)

        # left side
        left_sum = nums[0]
        left_dict = {}  # to record left side sum
        for i in range(1, N - 5):
            left_sum += nums[i]
            left_dict[i] = left_sum

        # right side
        right_sum = nums[N-1]
        right_dict = {}  # to record right side sum
        for i in range(N - 2, 4, -1):
            right_sum += nums[i]
            right_dict[i] = right_sum

        for i in
        print(left_dict)
        print(right_dict)
        return False

    def match_sum(self, nums, i, j, k, n):
        if sum(nums[0:i]) == sum(nums[i+1:j]) == sum(nums[j+1:k]) == sum(nums[k+1:n]):
            return True
        else:
            return False
