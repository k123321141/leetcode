class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:  # noqa
        '''
        Time complexity: O(nlogn)
        Space complexity: O(n)
        '''
        coherence = 0
        ret = 0
        arr = []
        for start, end in intervals:
            arr.append((start, 1))
            arr.append((end, -1))

        for _, count in sorted(arr):
            coherence += count
            if coherence > ret:
                ret = coherence
        return ret
