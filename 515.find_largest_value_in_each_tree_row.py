# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:  # noqa
        '''
        Run an BFS while recoding max value during the travel.
        Time: O(N), capacity: O(N)
        '''
        if root is None:
            return []

        Q = deque()
        Q.append((root, 0))
        depth_dict = {}

        while Q:
            node, depth = Q.popleft()
            depth_dict[depth] = max(depth_dict.get(depth, float('-inf')), node.val)
            if node.left is not None:
                Q.append((node.left, depth + 1))
            if node.right is not None:
                Q.append((node.right, depth + 1))

        ret = [depth_dict[depth] for depth in range(len(depth_dict))]
        return ret
