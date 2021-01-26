class Solution:
    '''
    If total product < 0 than divide by the less tail. (left or right)
    If array contains zero, seperatre array by zero and find the maximum product of each array.
    '''
    def maxProduct(self, nums: List[int]) -> int: # noqa
        # one pass 94%
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        # split by zero
        i = 0
        while nums[i] == 0:
            i += 1

        ans = 0 if i > 0 else float('-inf')
        product = left = right = nums[i]

        j = i+1
        while j < len(nums):
            if nums[j] == 0:
                leng = j-i
                ans = 0 if 0 > ans else ans
                if leng == 1:
                    ans = nums[i] if nums[i] > ans else ans
                elif leng > 1:
                    if product > 0:
                        ans = product if product > ans else ans
                    else:
                        # ret = self.foo(nums[i:j], product, left)
                        ret = product // (left if left >  right else right)
                        ans = ret if ret > ans else ans
                i = j+1
                while i < len(nums) and nums[i] == 0:
                    i += 1
                if i < len(nums):
                    product = left = right = nums[i]

                j = i+1
            else:
                product *= nums[j]
                if left > 0:
                    left = product
                if nums[j] < 0:
                    right = nums[j]
                else:
                    right *= nums[j]
                j += 1

        if nums[-1] != 0:
            if i == len(nums)-1:
                ans = nums[i] if nums[i] > ans else ans
            elif product > 0:
                ans = product if product > ans else ans
            else:
                ret = product // max(left, right)
                ans = ret if ret > ans else ans
        return ans
