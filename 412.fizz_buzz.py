class Solution:
    def fizzBuzz(self, n: int) -> List[str]:  # noqa
        ret = []
        count_3 = 3
        count_5 = 5
        for i in range(n):
            count_3 -= 1
            count_5 -= 1
            if count_3 == 0:
                count_3 = 3
                if count_5 == 0:
                    ret.append('FizzBuzz')
                    count_5 = 5
                else:
                    ret.append('Fizz')
            elif count_5 == 0:
                ret.append('Buzz')
                count_5 = 5

        return ret
