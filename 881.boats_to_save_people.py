class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:  # noqa
        '''Sort arr first, then scan with from both sides, head and tail.
        O(N logN)
        '''
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i < j:
            if people[i] + people[j] <= limit:
                count += 1
                i += 1
                j -= 1
            else:
                j -= 1

        return len(people) - count
