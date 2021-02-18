# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:  # noqa
        '''
        Run a pre-order traversal and keep tracking depth.
        '''
        if root is None:
            return []
        from collections import deque
        Q = deque()
        Q.append((root, 0))
        max_depth = float('-inf')
        while Q:
            node, depth = Q.popleft()
            max_depth = depth if depth > max_depth else max_depth
            if node.left:
                Q.append((node.left, depth+1))
            if node.right:
                Q.append((node.right, depth+1))
        return max_depth
