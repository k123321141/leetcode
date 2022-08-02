# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:  # noqa
        '''
        DFS search, O(N)
        '''
        if root is None:
            return []
        ans = []
        Q = deque()
        Q.append((root, 0, []))
        while Q:
            node, accum, path = Q.pop()
            new_path = path + [node.val, ]
            if node.left is None and node.right is None:  # leaf
                if node.val + accum == targetSum:
                    ans.append(new_path)
            if node.left:
                Q.append((node.left, accum + node.val, new_path))
            if node.right:
                Q.append((node.right, accum + node.val, new_path))
        return ans
