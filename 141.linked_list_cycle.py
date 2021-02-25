# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:  # noqa
        '''
        Reverse all link, if there is cycle exist, it will be point back to head.
        '''
        if head is None or head.next is None:
            return False
        pre, node = head, head.next
        head.next = None
        while node.next:
            node.next, node, pre = pre, node.next, node
        return head == node
