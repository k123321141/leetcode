# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:  # noqa
        '''
        Run a reversed BFS

        '''
        if root is None:
            return []
        Q = deque()
        Q.append((root, 0))
        pyramid = defaultdict(list)

        visited = set()
        while Q:
            node, depth = Q.popleft()
            pyramid[depth].append(node.val)

            if node.left and node.left not in visited:
                visited.add(node.left)
                Q.append((node.left, depth + 1))

            if node.right and node.right not in visited:
                visited.add(node.right)
                Q.append((node.right, depth + 1))

        ret = []
        for depth in range(max(pyramid.keys()), -1, -1):
            ret.append(pyramid[depth])
        return ret
