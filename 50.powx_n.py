class Solution:
    def myPow(self, x: float, n: int) -> float:

        return x ** n 

    def dp(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x * x
        elif n == -1:
            return 1. / x
        elif n < -1:
            return 1. / self.dp(x, -1*n)
        else:
            return self.dp(x*x, n // 2) * self.dp(x, n % 2)
