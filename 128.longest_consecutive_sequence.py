class ptr:
    def __init__(self, l=0):
        self.len = l
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'ptr-'+str(self.len)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  # noqa
        if len(nums) <= 1:
            return len(nums)
        '''
        Use a hash map to simulate bin which represent valid extension.
        '''
        from collections import defaultdict
        bin_dict = defaultdict(ptr)
        max_len = float('-inf')
        for n in nums:
            if bin_dict[n].len == 0:
                # miss
                if bin_dict[n-1].len == 0 and bin_dict[n+1].len == 0:
                    bin_dict[n] = ptr(1)
                    max_len = max(max_len, 1)
                # concat
                elif bin_dict[n-1].len > 0 and bin_dict[n+1].len > 0:
                    total_len = bin_dict[n-1].len + 1 + bin_dict[n+1].len
                    bin_dict[n-1].len = total_len
                    bin_dict[n+1].len = total_len
                    bin_dict[n] = bin_dict[n-1]
                    max_len = max(max_len, total_len)
                # extend
                elif bin_dict[n-1].len > 0:
                    total_len = bin_dict[n-1].len + 1
                    bin_dict[n-1].len = total_len
                    bin_dict[n] = bin_dict[n-1]
                    max_len = max(max_len, total_len)
                # extend
                elif bin_dict[n+1].len > 0:
                    total_len = bin_dict[n+1].len + 1
                    bin_dict[n+1].len = total_len
                    bin_dict[n] = bin_dict[n+1]
                    max_len = max(max_len, total_len)
                else:
                    raise Exception('No such case')
            else:
                pass
            for n in nums:
                print(f'{n}: {bin_dict[n]}.len')
        print(n, bin_dict)
        return max_len
