"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':  # noqa: F821
        '''Run a VLR traversal to record node index. O(N), mem O(log(N))'''
        self.depth_dict = {}
        self.LRV(root, 1)
        return root

    def LRV(self, root, depth):
        if root:
            self.LRV(root.left, depth + 1)
            self.LRV(root.right, depth + 1)
            if depth in self.depth_dict:
                self.depth_dict[depth].next = root
            self.depth_dict[depth] = root
