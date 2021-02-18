# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:  # noqa
        return self.dp(root, float('-inf'), float('inf'))

    def dp(self, root: TreeNode, low: int, high: int) -> bool:  # noqa
        if root.left is None and root.right is None:
            return low < root.val < high
        elif root.left is None:
            return root.right.val > root.val and low < root.val < high and self.dp(root.right, root.val, high)
        elif root.right is None:
            return root.left.val < root.val and low < root.val < high and self.dp(root.left, low, root.val)
        else:
            return root.left.val < root.val and root.right.val > root.val and low < root.val < high and self.dp(root.left, low, root.val) and self.dp(root.right, root.val, high)
