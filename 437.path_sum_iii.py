# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:  # noqa
        '''
        DFS search, O(N^2)
        '''
        if root is None:
            return 0
        ans = 0
        Q = deque()
        Q.append((root, []))
        while Q:
            node, path = Q.pop()
            new_path = path + [node.val, ]

            ans += self.search_path(new_path, targetSum)
            if node.left:
                Q.append((node.left, new_path))
            if node.right:
                Q.append((node.right, new_path))
        return ans

    def search_path(self, path: list, targetSum: int) -> int:  # noqa
        # rightest value is new-appended.
        N = len(path)
        ret = 0
        accum = 0
        for i in range(N-1, -1, -1):
            accum += path[i]
            if accum == targetSum:
                ret += 1
        return ret
