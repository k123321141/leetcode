from collections import deque


class Solution:
    '''
    Given an index, recusive solve whether the sub string which starts from index is valid.
    NOTE: BFS will cause timeout
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: # noqa
        if s is None:
            return False
        elif len(s) == 0:
            return False
        else:
            visited = set()
            stk = deque()

            stk.append(0)
            visited.add(0)
            while stk:
                idx = stk.pop()
                visited.add(idx)
                if idx == len(s):
                    return True
                elif idx < len(s):
                    for w in wordDict:
                        if s[idx:idx+len(w)] == w and idx+len(w) not in visited:
                            stk.append(idx+len(w))
            return False
