# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        a, b = rand7()-1, rand7()-1  # noqa
        x = 7 * a + b  # 0-48
        if x < 40:
            return (x % 10) + 1
        else:
            return self.rand10_offset(x - 40)

    def rand10_offset(self, offset: int):

        a, b = rand7()-1, rand7()-1  # noqa
        x = 7 * a + b + offset
        upper = ((48 + offset) // 10) * 10
        if x < upper:
            return (x % 10) + 1
        else:
            return self.rand10_offset(x - upper)
