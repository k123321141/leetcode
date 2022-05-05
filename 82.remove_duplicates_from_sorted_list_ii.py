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
        # check head
        while head.next and  head.val == head.next.val:
            val = head.val
            head = head.next.next
            if head:
                while head.val == val:
                    head = head.next
                    if head is None:
                        return None
            else:
                return None
        start = head
        pre_head = head
        head = head.next
        while head:
            if head.next and head.next.val == head.val:
                val = head.val
                head = head.next.next
                while head and head.val == val:
                    head = head.next
                if head is None or head.next is None:
                    pre_head.next = head
            else:
                pre_head.next = head
                pre_head = head
                head = head.next
        return start
