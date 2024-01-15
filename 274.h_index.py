class Solution:
    def hIndex(self, citations: List[int]) -> int:  # noqa
        '''Use Counting sort with accumulative sum
        time complexity: O(n)
        space complexity: O(1000) = O(1)
        '''
        arr = [0] * 1001
        for n in citations:
            arr[n] += 1

        accum = 0
        for i in range(len(arr) - 1, -1, -1):
            accum += arr[i]
            if i >= accum:
                return i
        return 0
