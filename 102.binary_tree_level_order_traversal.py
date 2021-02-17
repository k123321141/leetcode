# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:  # noqa
        '''
        Run a pre-order traversal and keep tracking depth.
        '''
        if root is None:
            return []
        from collections import deque, defaultdict
        Q = deque()
        Q.append((root, 0))
        depth_dict = defaultdict(list)
        while Q:
            node, depth = Q.popleft()
            depth_dict[depth].append(node.val)
            if node.left:
                Q.append((node.left, depth+1))
            if node.right:
                Q.append((node.right, depth+1))
        return list([depth_dict[dep] for dep in sorted(depth_dict)])
