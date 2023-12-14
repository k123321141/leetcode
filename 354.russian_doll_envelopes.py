from functools import cache
from bisect import bisect_right


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int: # noqa
        if len(envelopes) == 1:
            return 1
        self.envelopes = envelopes
        self.envelopes.sort()
        return max([self.dp(w, h) for w, h in self.envelopes])

    @cache
    def dp(self, width: int, height: int) -> int:
        max_depth = 1
        idx = bisect_right(self.envelopes, [width-1, height-1])
        for w, h in self.envelopes[:idx]:
            if h < height:
                max_depth = max(self.dp(w, h)+1, max_depth)
        return max_depth
