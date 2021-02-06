from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # noqa
        if len(strs) <= 1:
            return [strs, ]
        anagram_dict = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagram_dict[key].append(s)
        return [S for S in anagram_dict.values()]
