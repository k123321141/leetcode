class Solution:
    def myPow(self, x: float, n: int) -> float:
        rest = 1
        while True:
            if n == 0:
                return 1
            elif n == 1:
                return x * rest
            elif n == 2:
                return x * x * rest
            elif n == -1:
                return 1. / x
            elif n < -1:
                return 1. / self.myPow(x, -1*n)
            else:
                if n % 2 == 1:
                    rest *= x
                x *= x
                n = n // 2
