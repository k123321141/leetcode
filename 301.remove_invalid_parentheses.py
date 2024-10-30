from functools import cache
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if Solution.is_valid(s):
            return [s]
        Q = deque([s])
        visited = set()
        ret = []
        while Q:
            s = Q.popleft()
            count = Solution.counting(s)
            tgt = '(' if count > 0 else ')'
            for i, c in enumerate(s):
                if c != tgt:
                    continue
                if i == 0:
                    rest = s[1:]
                elif i == len(s) - 1:
                    rest = s[:-1]
                else:
                    rest = s[:i] + s[i + 1:]
                if Solution.is_valid(rest):
                    ret.append(rest)
                # no answer found yet
                elif len(ret) == 0:
                    if rest not in visited:
                        Q.append(rest)
                        visited.add(rest)
                # avoid too short answer
                elif len(rest) > len(ret[0]):
                    if rest not in visited:
                        Q.append(rest)
                        visited.add(rest)
        return list(set(ret))

    @cache
    @staticmethod
    def is_valid(s: str) -> bool:
        count = 0
        for c in s:
            if c == '(':
               count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    @cache
    @staticmethod
    def counting(s: str) -> int:
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return count
