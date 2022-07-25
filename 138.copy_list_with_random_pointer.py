"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':  # noqa
        '''
        2-pass version, O(N) space
        '''
        if head is None:
            return None
        to_be_annouce_arr = []

        idx_dict = {}
        node_dict = {}
        idx = 0
        new_head = pre = None
        while head:
            idx_dict[head] = idx
            new_node = Node(head.val)  # noqa
            if pre:
                pre.next = new_node
            if new_head is None:
                new_head = new_node

            node_dict[idx] = new_node
            if head.random:
                if head.random not in idx_dict:
                    to_be_annouce_arr.append((new_node, head.random))
                else:
                    new_node.random = node_dict[idx_dict[head.random]]

            head = head.next
            pre = new_node
            idx += 1
        for new_node, node in to_be_annouce_arr:
            idx = idx_dict[node]
            new_node.random = node_dict[idx]
        return new_head
