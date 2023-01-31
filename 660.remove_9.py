from functools import cache
import math


class Solution:
    def newInteger(self, n: int) -> int:
        target_n = n
        while True:
            count = Solution.exclude_9(target_n)
            if count == n:
                return target_n
            else:
                target_n += n - count

    @staticmethod
    @cache
    def exclude_9(n: int) -> int:
        """exclude_9.

        Return how many integers that doesn't contain 9.

        Parameters
        ----------
        n : int
            n

        Returns
        -------
        int

        """
        return n - Solution.include_9(n)

    @staticmethod
    @cache
    def include_9(n: int) -> int:
        s = str(n)
        ret = 0
        flag_9 = False
        for i, v in enumerate(s[:-1]):
            if v == '0':
                continue
            if flag_9:
                ret += int(s[i:])
                return ret

            power = len(s) - 1 - i
            count_9 = Solution.ten_base(power) * int(v)

            count_9 += 1 if v == '9' else 0
            ret += count_9

            if v == '9':
                flag_9 = True

        # last digit
        if flag_9:
            ret += int(s[-1])
        else:
            ret += 1 if s[-1] == '9' else 0
        return ret

    @staticmethod
    @cache
    def c(a: int, b: int) -> int:
        upper = 1
        lower = 1
        for i in range(b):
            upper *= a - i
            lower *= (i + 1)
        return int(upper / lower)

    @staticmethod
    @cache
    def ten_base(power: int) -> int:
        if power == 0:
            return 1
        else:
            ret = 0
            for i in range(power):
                ret += Solution.c(power, i+1) * math.pow(9, power - 1 - i)
            return int(ret)
