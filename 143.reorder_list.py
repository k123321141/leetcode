# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None: # noqa
        """
        Do not return anything, modify head in-place instead.
        
        2-pass array index
        """
        if head is None or head.next is None:
            return head
        arr = []
        ptr = head
        while ptr is not None:
            arr.append(ptr)
            ptr = ptr.next
        i, j = 0, len(arr)-1

        ptr = head
        while i < j:
            if i == 0:
                ptr = head
            else:
                ptr.next = arr[i]
                ptr = arr[i]
            ptr.next = arr[j]
            ptr = arr[j]
            i += 1
            j -= 1
        if i == j:
            ptr.next = arr[i]
            ptr.next.next = None
        else:
            ptr.next = None
        return head
