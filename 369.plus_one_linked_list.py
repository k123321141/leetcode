# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:  # noqa
        reverse_dict = {}
        cursor = head
        reverse_dict[head] = None
        while cursor.next is not None:
            reverse_dict[cursor.next] = cursor
            cursor = cursor.next

        while reverse_dict[cursor] is not None:
            if cursor.val < 9:
                cursor.val += 1
                return head
            else:
                cursor.val = 0
                cursor = reverse_dict[cursor]
        if cursor == head and head.val < 9:
            head.val += 1
            return head

        cursor.val = 0
        head = ListNode(1, cursor)  # noq
        return head
