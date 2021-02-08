from functools import lru_cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:  # noqa
        self.h, self.w = len(obstacleGrid), len(obstacleGrid[0])
        self.mat = obstacleGrid
        if self.mat[0][0] == 1:
            return 0
        else:
            return self.dp(0, 0)

    @lru_cache
    def dp(self, y: int, x: int):
        if y == self.h-1:
            for i in range(x, self.w):
                if self.mat[y][i] == 1:
                    return 0
            return 1
        elif x == self.w-1:
            for i in range(y, self.h):
                if self.mat[i][x] == 1:
                    return 0
            return 1
        else:
            ret = 0
            if self.mat[y+1][x] == 0:
                ret += self.dp(y+1, x)
            if self.mat[y][x+1] == 0:
                ret += self.dp(y, x+1)
            return ret
