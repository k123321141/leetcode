class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  # noqa
        if len(nums) <= 1:
            return len(nums)
        '''
        Use a hash map to simulate bin which represent valid extension.
        Every key store a left/right pair.
        '''
        bin_dict = {}
        max_len = float('-inf')
        for n in nums:
            if n not in bin_dict:
                # miss
                if n-1 not in bin_dict and n+1 not in bin_dict:
                    bin_dict[n] = [n, n]
                    max_len = max(max_len, 1)
                # concat
                elif n-1 in bin_dict and n+1 in bin_dict:
                    l, r = bin_dict[n-1][0], bin_dict[n+1][1]
                    bin_dict[r][0] = l
                    bin_dict[l][1] = r
                    bin_dict[n] = True
                    max_len = max(max_len, r-l+1)
                # extend right
                elif n-1 in bin_dict:
                    l, r = bin_dict[n-1][0], n
                    bin_dict[l][1] = r
                    bin_dict[n] = [l, r]
                    max_len = max(max_len, r-l+1)
                # extend left
                elif n+1 in bin_dict:
                    l, r = n, bin_dict[n+1][1]
                    bin_dict[r][0] = l
                    bin_dict[n] = [l, r]
                    max_len = max(max_len, r-l+1)
                else:
                    raise Exception('No such case')
            else:
                pass
        return max_len
