class Solution:
    '''
    If total product < 0 than divide by the less tail. (left or right)
    If array contains zero, seperatre array by zero and find the maximum product of each array.
    '''
    def maxProduct(self, nums: List[int]) -> int: # noqa
        # recusive 34%
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        # split by zero
        i = 0
        zero_flag = False
        ans_arr = []

        for j in range(len(nums)):
            if nums[j] == 0:
                zero_flag = True
                if j-i > 0:
                    ans_arr.append(self.foo(nums[i:j]))
                i = j+1
        if nums[-1] != 0:
            ans_arr.append(self.foo(nums[i:]))
        if zero_flag:
            ans_arr.append(0)
        return max(ans_arr)

    def foo(self, nums: List[int]) -> int: # noqa
        if len(nums) == 1:
            return nums[0]
        product = 1
        for i, n in enumerate(nums):
            product *= n
        if product > 0:
            return product
        else:
            # find the less tail
            left = nums[0]
            i = 1
            while left > 0:
                left *= nums[i]
                i += 1

            right = nums[-1]
            i = len(nums)-2
            while right > 0:
                right *= nums[i]
                i -= 1
            # print(product, left, right)
            return product // max(left, right)
