from heapq import heappush, heappop, heappushpop


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:  # noqa
        '''
        Use a heap to store the height difference between each two adjacent buildings.
        Time: O(N logN)
        '''
        heap = []
        accum = 0
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            else:
                # use ladder if possible
                accum += diff
                if accum > bricks:
                    pop_diff = -1 * heappushpop(heap, -diff)
                    accum -= pop_diff
                    ladders -= 1
                    if ladders < 0:
                        return i

                    while accum > bricks:
                        pop_diff = -1 * heappop(heap)
                        accum -= pop_diff
                        ladders -= 1
                        if ladders < 0:
                            return i
                else:
                    heappush(heap, -diff)
        return len(heights) - 1
