# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  # noqa
        """
        Keep the lower node trace its parent.
        O(N)
        """
        parent_dict, p_depth, q_depth = self.bfs(root, p, q)

        while p != q:
            if p_depth > q_depth:
                p = parent_dict[p]
                p_depth -= 1
            else:
                q = parent_dict[q]
                q_depth -= 1
        return p


    def bfs(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):  # noqa
        parent_dict = {}
        Q = deque([(root, root, 0), ])

        p_found = False
        q_found = False

        while Q:
            parent, node, depth = Q.popleft()
            parent_dict[node] = parent

            if node == p:
                p_found = True
                p_depth = depth
            elif node == q:
                q_found = True
                q_depth = depth

            early_break = p_found and q_found
            if early_break:
                break

            if node.left:
                Q.append((node, node.left, depth + 1))
            if node.right:
                Q.append((node, node.right, depth + 1))

        return parent_dict, p_depth, q_depth
