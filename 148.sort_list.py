# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # noqa
        '''
        It's merge sort.
        '''

        # get array length
        n = 0 if head is None else 1
        if n == 0:
            return None
        node = head
        while node.next:
            node = node.next
            n += 1
        # get depth
        for depth in range(math.ceil(math.log2(n))):
            left_node = pre_head = head
            length = int(math.pow(2, depth))
            while left_node:  # break as iter reach the last node
                # get right node
                right_node = left_node
                for _ in range(length):
                    right_node = right_node.next
                    if right_node is None:
                        break
                if right_node is None:
                    break

                # get len_2
                len_2 = 0
                tail = right_node
                for _ in range(length):
                    tail = tail.next
                    len_2 += 1
                    if tail is None:
                        break
                if left_node == head:
                    head, pre_head = Solution.merge_two_sorted_list(None, left_node, length, right_node, len_2)
                else:
                    _, pre_head = Solution.merge_two_sorted_list(pre_head, left_node, length, right_node, len_2)
                left_node = tail

        return head

    def merge_two_sorted_list(head: ListNode, head_1: ListNode, len_1: int, head_2: ListNode, len_2: int):  # noqa
        iter_count_1 = iter_count_2 = 0
        if head is None:
            if head_2.val < head_1.val:
                head = head_2
                iter_count_2 += 1
                head_2 = head_2.next
            else:
                head = head_1
                iter_count_1 += 1
                head_1 = head_1.next
        first_node = head

        for i in range(len_1 + len_2 - iter_count_1 - iter_count_2):
            if iter_count_1 == len_1:
                last_node = head_2
                for _ in range(len_2 - 1 - iter_count_2):
                    last_node = last_node.next
                return first_node, last_node
            elif iter_count_2 == len_2:
                tmp = head.next
                head.next = head_1
                last_node = head_1
                for _ in range(len_1 - 1 - iter_count_1):
                    last_node = last_node.next
                last_node.next = tmp
                return first_node, last_node
            elif head_2.val < head_1.val:
                head.next = head_2
                iter_count_2 += 1
                head, head_2 = head.next, head_2.next
            else:
                head.next = head_1
                iter_count_1 += 1
                head, head_1 = head.next, head_1.next
        return first_node, head
