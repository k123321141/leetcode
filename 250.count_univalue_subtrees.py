# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:  # noqa
        '''
        Top-down O(N)
        '''
        if root is None:
            return 0
        self.count = 0
        self._valid(root)
        return self.count

    def _valid(self, node: Optional[TreeNode]) -> bool:  # noqa
        ret = True
        if node.left:
            condi = self._valid(node.left)
            ret = ret and condi and node.val == node.left.val
        if node.right:
            condi = self._valid(node.right)
            ret = ret and condi and node.val == node.right.val
        if ret:
            self.count += 1
        return ret
