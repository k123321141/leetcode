# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:  # noqa
        '''
        O(N), DFS
        '''

        Q = deque()
        Q.append((root, 1))
weff        ret = float('-inf')
        while Q:
            node, length = Q.pop()
            if length > ret:
                ret = length
            if node.left:
                if node.left.val == node.val + 1:
                    Q.append((node.left, length + 1))
                else:
                    Q.append((node.left, 1))

            if node.right:
                if node.right.val == node.val + 1:
                    Q.append((node.right, length + 1))
                else:
                    Q.append((node.right, 1))
        return ret
