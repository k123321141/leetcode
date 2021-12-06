from typing import List
from functools import lru_cache


@lru_cache
def dp(s):
    if len(s) == 1:
        return [s, ]
    elif len(s) == 2:
        return [s[0], s[1]]
    if s[0] == '0':
        return [0] + dp(s[1:])

    ret = []
    ret.extend()
    return ret


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]

        if len(s) == 2:
            x = s[0]
            y = s[1]
            return [f'({x}, {y})']
        ret = []
        for comma_idx in range(1, len(s)):
            left = s[0:comma_idx]
            right = s[comma_idx:]
            for left_dot_idx in range(len(left)):
                if left_dot_idx == 0:
                    x = left
                    if not Solution.is_valid_int(x):
                        continue
                else:
                    if Solution.is_valid_int(left[:left_dot_idx]) and Solution.is_valid_float(left[left_dot_idx:]):
                        x = left[:left_dot_idx] + '.' + left[left_dot_idx:]
                    else:
                        continue
                for right_dot_idx in range(len(right)):
                    if right_dot_idx == 0:
                        y = right
                        if not Solution.is_valid_int(y):
                            continue
                    else:
                        if Solution.is_valid_int(right[:right_dot_idx]) and Solution.is_valid_float(right[right_dot_idx:]):
                            y = right[:right_dot_idx] + '.' + right[right_dot_idx:]
                        else:
                            continue
                    ret.append(f'({x}, {y})')
        return ret

    @staticmethod
    def is_valid_int(s):
        return not(len(s) > 1 and s[0] == '0')

    @staticmethod
    def is_valid_float(s):
        return s[-1] != '0'
