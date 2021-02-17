class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        import re
        pat = re.compile(r'[^a-z0-9]+')
        s = re.sub(pat, '', s.lower())
        if len(s) == 0:
            return True
        l, r = 0, len(s)-1
        while r-l > 0:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
