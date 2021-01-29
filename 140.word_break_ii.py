from collections import deque


class Solution:
    '''
    refer to 139.
    DFS, early prune the invalid node.
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: # noqa
        if s is None:
            return False
        elif len(s) == 0:
            return False
        else:
            # check valid char set:
            if len(s) > 7:
                input_set = set(s)
                word_set = set()
                for w in wordDict:
                    for c in w:
                        word_set.add(c)
                if not input_set.issubset(word_set):
                    return []
            #
            ret = []
            Q = deque()

            valid = {}
            Q.append((0, '0 ', ''))

            while Q:
                idx, idx_prefix, prefix = Q.pop()
                if idx == len(s):
                    ret.append(prefix[:-1])
                    for i in idx_prefix[:-1].split(' '):
                        valid[int(i)] = True
                elif idx < len(s):
                    aleast_one_match = False
                    for w in wordDict:
                        if s[idx:idx+len(w)] == w:
                            aleast_one_match = True
                            next_idx = idx+len(w)
                            if next_idx not in valid or valid[next_idx]:
                                Q.append((idx+len(w), f'{idx_prefix}{idx} ', f'{prefix}{w} '))
                    if not aleast_one_match:
                        valid[idx] = False
                        # print(f'prune: {s[:idx]} | {s[idx:]}')
            # print(valid)
            return ret
# Test Input
# "carscars"
# ["ca", "rs", "car", "sca"]
# 4 [ca rs]
# 3 [sca rs]
# 2 [rs ca rs]
# 0 [ca re ca re, car sca ]
