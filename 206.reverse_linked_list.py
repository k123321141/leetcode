# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode: # noqa
        if head is None or head.next is None:
            return head
        pre = None
        while head.next:
            buf = head.next
            head.next = pre
            pre = head
            head = buf

        head.next = pre
        return head
