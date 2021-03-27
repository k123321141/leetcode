class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        rows = [[] for i in range(numRows)]

        y = 0
        x = 0
        is_zig = True
        for i, w in enumerate(s):
            if is_zig:
                rows[y].append(w)
                if y == numRows - 1:
                    y -= 1
                    x += 1
                    is_zig = False
                else:
                    y += 1
            else:
                if y == 0:
                    rows[y].append(w)
                    y += 1
                    is_zig = True
                else:
                    for j in range(numRows):
                        if j == y:
                            rows[j].append(w)
                        else:
                            rows[j].append(' ')
                    y -= 1
                    x += 1
        ret = ''
        for row in rows:
            print(row)
            ret += ''.join(row).replace(' ', '')
        return ret
