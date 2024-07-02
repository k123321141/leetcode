class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # noqa
        '''
        Scan it twice in forward and backward.
        O(2N)
        '''
        product = nums[-1]
        backward_product = [product,]
        for v in reversed(nums[1:-1]):
            product *= v
            backward_product.append(product)

        ret = [product, ]
        product = nums[0]
        N = len(backward_product)
        for i, v in enumerate(nums[1:-1]):
            val = product * backward_product[N - 2 - i]
            ret.append(val)
            product *= v
        ret.append(product)
        return ret
