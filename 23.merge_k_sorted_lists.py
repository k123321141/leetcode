# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode: # noqa
        '''
        merge sort.
        N log K
        '''
        lists = [l for l in lists if l is not None]
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            lists[0].len = lists[1].len = 1
            return self.mergeTwoLists(lists[0], lists[1])[0]
        else:
            # queue version 55%
            '''
            from collections import deque
            Q = deque(lists)
            while len(Q) > 1:
                l1 = Q.popleft()
                l2 = Q.popleft()
                head = self.mergeTwoLists(l1, l2)
                Q.append(head)
            return Q.pop()
            '''
            # heap sor 93%t
            import heapq
            Q = []
            idx = 0
            for node in lists:
                while node is not None:
                    heapq.heappush(Q, (node.val, idx, node))
                    idx += 1
                    node = node.next
            _, _, root = heapq.heappop(Q)
            head = root
            while len(Q) > 0:
                _, _, node = heapq.heappop(Q)
                head.next = node
                head = node
            return root

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: # noqa
        src_l1, src_l2 = l1, l2
        if l1.val <= l2.val:
            head = ptr = l1
            l1 = l1.next
        else:
            head = ptr = l2
            l2 = l2.next
        leng = 2
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
            leng += 1
        if l1 is None and l2 is not None:
            ptr.next = l2
        elif l1 is not None and l2 is None:
            ptr.next = l1
        return head, max(leng, src_l1.len, src_l2.len)
