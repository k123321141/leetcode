# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:  # noqa
        if head is None or head.next is None:
            return head
        start = head
        while head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return start
