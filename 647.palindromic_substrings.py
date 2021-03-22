class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Look up table. 6.56%
        '''
        ret = 0
        self.cache = {}
        for i in range(len(s)):
            for j in reversed(range(i+1, len(s)+1)):
                if self.is_palindrome_with_cache(s[i:j]):
                    ret += 1
        return ret

    def is_palindrome_with_cache(self, s) -> bool:
        cache = self.cache
        if s in cache:
            return cache[s]
        else:
            ret = Solution.is_palindrome(s)
            cache[s] = ret
            if len(s) > 2 and ret:
                l, r = 1, len(s) - 1
                while l < r:
                    cache[s[l:r]] = True
                    l += 1
                    r -= 1
            return ret

    @staticmethod
    def is_palindrome(s: str) -> bool:
        if len(s) == 1:
            return True
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
