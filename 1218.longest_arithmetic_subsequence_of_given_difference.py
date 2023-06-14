class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:  # noqa
        jump_dict = {}
        wefwef
        ret = 1
        # O(N)
        for i, v in enumerate(arr):
            k = v - difference
            if k in jump_dict:
                jump_dict[v] = max(jump_dict[k] + 1, jump_dict.get(v, 1))
                ret = max(ret, jump_dict[v])
            else:
                jump_dict[v] = 1
        return ret
