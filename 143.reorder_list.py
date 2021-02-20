# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None: # noqa
        """
        Do not return anything, modify head in-place instead.

        Find the middle node. (turtle rabbit race)
        """
        if head is None or head.next is None:
            return head

        turtle = rabbit = head
        while rabbit.next is not None:
            turtle = turtle.next
            rabbit = rabbit.next
            if rabbit.next is None:
                break
            else:
                rabbit = rabbit.next
        # reverse nodes after middle node
        pre = mid = turtle
        turtle = turtle.next
        while turtle is not None:
            turtle.next, turtle, pre = pre, turtle.next, turtle

        # reorder
        ptr = head
        while rabbit != mid:
            buf = ptr.next
            ptr.next, ptr = rabbit, buf

            buf = rabbit.next
            rabbit.next, rabbit = ptr, buf
        if ptr == rabbit:
            ptr.next = None
        else:
            rabbit.next = None
            ptr.next = rabbit
        return None
