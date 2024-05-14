class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:  # noqa
        arr = []
        idx_arr = []
        accum = 0
        total = 0
        idx = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            diff = g - c
            total += diff
            accum += diff
            if accum < 0 and i < (len(gas) - 1):
                arr.append(accum)
                accum = 0
                idx_arr.append(idx)
                idx = i + 1
        arr.append(accum)
        idx_arr.append(idx)
        if total < 0:
            return -1
        for i in reversed(range(len(arr))):
            if self.simulate(arr, i):
                return idx_arr[i]
        return -1

    def simulate(self, arr: list, index: int) -> bool:
        accum = 0
        for i in range(index, len(arr)):
            accum += arr[i]
            if accum < 0:
                return False
        for i in range(index):
            accum += arr[i]
            if accum < 0:
                return False
        return True
