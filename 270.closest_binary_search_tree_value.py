# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:  # noqa
        min_diff = float('inf')
        ret = root
        while root is not None:
            diff = abs(root.val - target)
            if diff < min_diff:
                min_diff = diff
                ret = root
            if target == root.val:
                return root.val
            elif target > root.val:
                root = root.right
            else:
                root = root.left
        return ret.val
