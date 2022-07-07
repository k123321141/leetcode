import math
from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        ret = self.dp(s)
        if ret == float('-inf'):
            ret = 0
        return ret

    @cache
    def dp(self, s):
        if len(s) == 0:
            return 1
        elif s.startswith('0'):
            return float('-inf')
        elif len(s) == 1:
            return 1
        else:
            # len(s) > 1
            c1 = self.dp(s[1:])
            ret = 0 if math.isinf(c1) else c1
            if s[0] in ['1', '2'] and int(s[:2]) <= 26:
                c2 = self.dp(s[2:])
                ret += 0 if math.isinf(c2) else c2
            return ret
