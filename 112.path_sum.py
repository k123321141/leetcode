# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:  # noqa
        '''
        DFS search, O(N)
        '''
        if root is None:
            return False
        Q = deque()
        Q.append((root, 0))
        while Q:
            node, accum = Q.pop()
            if node.left is None and node.right is None:  # leaf
                if node.val + accum == targetSum:
                    return True
            if node.left:
                Q.append((node.left, accum + node.val))
            if node.right:
                Q.append((node.right, accum + node.val))
        return False
