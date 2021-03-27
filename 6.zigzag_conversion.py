class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
    ['0', ' ', ' ', ' ', '8', ' ', ' ', ' ', '16', ' ', ' ', ' ', '24']
    ['1', ' ', ' ', '7', '9', ' ', ' ', '15', '17', ' ', ' ', '23', '25']
    ['2', ' ', '6', ' ', '10', ' ', '14', ' ', '18', ' ', '22', ' ']
    ['3', '5', ' ', ' ', '11', '13', ' ', ' ', '19', '21', ' ', ' ']
    ['4', ' ', ' ', ' ', '12', ' ', ' ', ' ', '20', ' ', ' ', ' ']
        '''

        if len(s) == 1 or numRows == 1:
            return s
        ret = []
        step_size = (numRows-1)*2
        for y in range(numRows):
            for i in range(y, len(s), step_size):
                ret.append(s[i])
                if 0 < y < numRows-1:
                    j = i + (step_size-2*y)
                    if j < len(s):
                        ret.append(s[j])
        return ''.join(ret)
