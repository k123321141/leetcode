class Solution:
    def findMinMoves(self, machines: List[int]) -> int:  # noqa

        if len(machines) <= 1:
            return 0

        count = sum(machines)
        n = len(machines)
        if count % n != 0:
            return -1
        avg = count // n

        # partition
        buf = machines[0]
        offset = 0
        return self.iter_loop(machines, avg)
        ret = float('inf')
        for i in range(1, n):
            buf += machines[i]
            if buf == avg * (i+1):
                sub = machines[offset:i+1]
                ret = min(self.iter_loop(sub, avg), ret)
                offset = i+1

        return ret

    def iter_acc(self, machines):
        left_side_sum = []

        accum = 0
        for x in machines:
            accum += x
            left_side_sum.append(accum)

        return left_side_sum

    def iter_loop(self, machines: List[int], avg: int) -> int:  # noqa
        n = len(machines)
        move_arr = [0] * n

        ret = 0
        while not self.is_balance(machines):
            left_side_sum = self.iter_acc(machines)

            for i, v in enumerate(machines):
                left_sum = left_side_sum[i] - v

                total = left_sum - (avg * i)

                # print(i, total)
                if v == 0:
                    pass
                elif i == 0:
                    if v > avg:
                        move_arr[i+1] += 1
                        move_arr[i] -= 1
                elif i == (n - 1):
                    if v > avg:
                        move_arr[i-1] += 1
                        move_arr[i] -= 1
                elif total == 0 and v > avg:
                    move_arr[i+1] += 1
                    move_arr[i] -= 1
                elif total < 0:
                    move_arr[i-1] += 1
                    move_arr[i] -= 1
                elif total > 0:
                    if total + (v - avg) > 0:
                        move_arr[i+1] += 1
                        move_arr[i] -= 1
                    else:
                        pass
            # print(machines)
            # print(move_arr)
            for i, v in enumerate(move_arr):
                machines[i] += v
                move_arr[i] = 0
            # print(machines)
            # print('-'*30)
            # if ret > 5:
                # break
            ret += 1
        return ret

    def is_balance(self, machines: List[int]) -> bool:  # noqa
        v0 = machines[0]
        for v in machines[1:]:
            if v != v0:
                return False
        return True
