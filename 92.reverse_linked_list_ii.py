# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode: # noqa
        if head is None or head.next is None or left == right:
            return head
        start = head
        for i in range(left-2):
            head = head.next
        if left == 1:

            pre = None
            for i in range(right - left + 1):
                buf = head.next
                head.next = pre
                pre = head
                head = buf
            start.next = head
            return pre
        else:
            left_head = head
            head = left_tail = head.next

            pre = None
            for i in range(right - left + 1):
                buf = head.next
                head.next = pre
                pre = head
                head = buf

            left_tail.next = head
            left_head.next = pre
            return start if left > 1 else pre
