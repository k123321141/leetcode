from functools import cache


class Solution:
    @cache
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
            ret = 0
            n = len(s)
            for i in range(n):
                if i == 0:
                    sub = s[1:]
                    ret += self.numDistinct(sub, t)
                elif i == (len(s)-1):
                    sub = s[:i]
                    ret += 1 if sub == t else 0
                else:
                    left = s[:i]
                    if t.startswith(left):
                        right = s[i+1:]
                        sub = left + right
                        ret += self.numDistinct(right, t[len(left):])
        return ret
