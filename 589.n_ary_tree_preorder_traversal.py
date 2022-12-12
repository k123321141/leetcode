"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def preorder(self, root: 'Node') -> List[int]:  # noqa
        if root is None:
            return None
        elif len(root.children) == 0:
            return [root.val, ]

        stk = deque()
        ret = []

        stk.append(root)
        while stk:
            node = stk.pop()

            ret.append(node.val)
            for child in reversed(node.children):
                stk.append(child)
        return ret
