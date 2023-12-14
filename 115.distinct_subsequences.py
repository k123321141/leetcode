from functools import cache


class Solution:
    # 98%
    def numDistinct(self, s: str, t: str) -> int:

        if s == t:
            ret = 1
        elif len(t) > len(s):
            ret = 0
        elif len(t) == 1:
            ret = 0
            for i, c in enumerate(s):
                if c == t[0]:
                    ret += 1
        else:
            self.s = s
            self.t = t
            return self.dp(0, 0)
        return ret

    @cache
    def dp(self, i: int, j: int) -> int:
        s = self.s
        t = self.t
        x = s[i]
        y = t[j]
        if (len(s) - i) < (len(t) - j):
            return 0
        elif j == (len(t)-1):
            ret = 0
            for idx in range(i, len(s)):
                ret += 1 if s[idx] == y else 0
        else:
            if x == y:
                ret = self.dp(i+1, j+1) + self.dp(i+1, j)
            else:
                ret = self.dp(i+1, j)
        return ret
