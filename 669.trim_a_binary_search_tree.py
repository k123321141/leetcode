# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:  # noqa
        '''
        O(N)
        Run a BFS while keep tracking valid parent.

        '''

        if root is None:
            return root
        valid_root = None
        Q = deque()

        Q.append([None, root])
        while Q:
            parent, node = Q.popleft()
            if node is not None:
                if low <= node.val <= high:
                    if valid_root is None:
                        valid_root = node
                    if parent is not None:
                        if node.val <= parent.val:
                            parent.left = node
                        else:
                            parent.right = node
                    parent = node
                else:
                    if parent is not None:
                        if node.val <= parent.val:
                            parent.left = None
                        else:
                            parent.right = None

                if node.val >= low:
                    Q.append([parent, node.left])
                if node.val <= high:
                    Q.append([parent, node.right])
        return valid_root
