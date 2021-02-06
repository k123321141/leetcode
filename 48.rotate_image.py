import math


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None: # noqa
        """
        Do not return anything, modify matrix in-place instead.
        If the dimension is even, flip 4 corner block along with diagonal and paste it to next block (clockwise).
        For odd dimension, move the vertical and horizontal axis additionally.
        """
        dim = len(matrix)
        m = matrix
        if dim == 1:
            pass
        elif dim == 2:
            m[0][0], m[0][1], m[1][0], m[1][1] = m[1][0], m[0][0], m[1][1], m[0][1]
        elif dim == 3:
            # corners
            m[0][0], m[0][2], m[2][2], m[2][0] = m[2][0], m[0][0], m[0][2], m[2][2]
            # axises
            m[0][1], m[1][2], m[2][1], m[1][0] = m[1][0], m[0][1], m[1][2], m[2][1]
        else:
            half = dim // 2
            pivot = int(math.ceil(dim/2))

            # 4 corner blocks
            self.flip(m, 0, 0, half)
            self.inverse_flip(m, pivot, 0, half)
            self.flip(m, pivot, pivot, half)
            self.inverse_flip(m, 0, pivot, half)
            # for row in m:
                # print(' '.join([f'{v:2d}'for v in row]))
            # print('\n------\n')

            buf = []
            # left-up to right-up
            for y in range(half):
                for x in range(half):
                    buf.append(m[y][x+pivot])
                    m[y][x+pivot] = m[y][half-x-1]
            # left-bot to left-up
            for y in range(half):
                for x in range(half):
                    m[y][x] = m[dim-y-1][x]
            # right-bot to left-bot
            for y in range(half):
                for x in range(half):
                    m[y+pivot][x] = m[y+pivot][dim-x-1]
            # right-up to right-bot
            i = 0
            for y in range(half-1, -1, -1):
                for x in range(half):
                    m[y+pivot][x+pivot] = buf[i]
                    i += 1
            # for row in m:
                # print(' '.join([f'{v:2d}'for v in row]))

            if pivot != half:  # odd dimension
                for i in range(1, half+1):
                    m[half][half+i], m[half-i][half], m[half][half-i], m[half+i][half] = m[half-i][half], m[half][half-i], m[half+i][half], m[half][half+i]



    def flip(self, m: List[List[int]], offset_x: int, offset_y: int, dim: int) -> None: # noqa
        for y in range(dim-1):
            for x in range(y+1, dim, 1):
                m[offset_y + y][offset_x + x], m[offset_x + x][offset_y + y] = m[offset_x + x][offset_y + y], m[offset_y + y][offset_x + x]

    def inverse_flip(self, m: List[List[int]], offset_x: int, offset_y: int, dim: int) -> None: # noqa
        for y in range(dim-1):
            for x in range(y, dim, 1):
                m[offset_y + dim-y-1][offset_x + x], m[offset_y + dim-x-1][offset_x + y] = m[offset_y + dim-x-1][offset_x + y], m[offset_y + dim-y-1][offset_x + x]
