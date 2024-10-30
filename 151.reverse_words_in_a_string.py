import re


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        pat = re.compile(r'\s+')
        arr = pat.split(s)
        # print(arr)
        ret = ' '.join(arr[::-1])
        return ret
