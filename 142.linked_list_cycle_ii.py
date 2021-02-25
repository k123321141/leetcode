# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:  # noqa
        '''
        rabbit turtle race
        '''
        if head is None or head.next is None:
            return None
        # cycle detect
        turtle = head
        rabbit = head
        while True:
            turtle = self.step(turtle, 1)
            rabbit = self.step(rabbit, 2)

            if rabbit is None:
                return None
            if turtle == rabbit:  # find cycle
                break
        # print(f'cycle {rabbit.val}')
        # cycle length detect
        leng = 0
        while True:
            leng += 1
            turtle = self.step(turtle, 1)
            rabbit = self.step(rabbit, 2)
            if turtle == rabbit:
                break
        # print(f'leng {leng}')

        # try to find begin
        pre = head
        current = self.step(pre, leng)
        next_step = self.step(current, leng)
        while current != next_step:
            pre = current
            current = next_step
            next_step = self.step(next_step, leng)
        # now pre pointer is not in cycle
        while pre != self.step(pre, leng):
            pre = self.step(pre, 1)

        return pre

    def step(self, head, step_size):
        assert step_size > 0
        ret = head
        for i in range(step_size):
            ret = ret.next
            if ret is None:
                return None
        return ret
