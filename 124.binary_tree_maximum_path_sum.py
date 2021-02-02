# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
from functools import lru_cache


class Solution:
    def maxPathSum(self, root: TreeNode) -> int: # noqa
        '''
        1. Keep tracking maximum value for every node that it can provide to its root.

            1
          2   3
        4   5

        7 will be the value for node 2.

        2. Calculate the sum for every node if the node be the pivot, e.g., 1 can be the pivot to connect left and right sub tree, and the sum will be 7 + 1 + 3.


        '''
        # dp version 43%
        if root is None:
            return 0
        self.max_sum = float('-inf')
        self.dp(root)
        return self.max_sum

    @lru_cache
    def dp(self, root: TreeNode) -> int: # noqa
        if root is None:
            return 0
        else:
            left_v = self.dp(root.left)
            right_v = self.dp(root.right)
            max_v = max(left_v, right_v) + root.val
            pivot_v = left_v + right_v + root.val
            self.max_sum = max(max_v, pivot_v, self.max_sum)

            return max_v if max_v > 0 else 0
