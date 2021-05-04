class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: # noqa
        '''
        Maintain a sliding window. O(n)
        '''
        if len(nums) == 1:
            return False
        k = min(k, len(nums))
        hash_dict = {}
        for i in range(k):
            n = nums[i]
            if n in hash_dict:
                return True
            else:
                hash_dict[n] = True

        left_idx = 0
        for i in range(k, len(nums)):

            n = nums[i]
            if n in hash_dict:
                if hash_dict[n]:
                    return True
                else:
                    hash_dict[n] = True
            else:
                hash_dict[n] = True
            hash_dict[nums[left_idx]] = False
            left_idx += 1
        return False
