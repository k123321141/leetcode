# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


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
        stk = deque()
        stk.append(root)
        arr = []
        while stk:
            node = stk.pop()
            arr.append(node)
            if node.right is not None:
                stk.append(node.right)
            if node.left is not None:
                stk.append(node.left)
        value_dict = {None: 0}
        max_sum = float('-inf')
        for node in arr[::-1]:
            l = value_dict[node.left]
            r = value_dict[node.right]
            v = max(l, r) + node.val
            value_dict[node] = max(0, v)
            max_sum = max(max_sum, v, l + r + node.val)
        return max_sum
