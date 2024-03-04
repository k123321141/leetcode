# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        if head is None or head.next is None:
            return head
        src_head = head.next
        prime = None
        while True:
            buf = head.next.next
            if prime is None:
                prime = head
            else:
                prime.next = head.next
                prime = head
            head.next.next = head
            head.next = buf
            head = head.next
            if head is None or head.next is None:
                break
        return src_head
