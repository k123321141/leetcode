# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:  # noqa
        if root is None:
            return []
        self.height = -1
        self.ret = []
        self.vrl(root, 0)
        return self.ret

    def vrl(self, root, height: int) -> None:
        if height > self.height:
            self.ret.append(root.val)
            self.height = height
        if root.right:
            self.vrl(root.right, height + 1)
        if root.left:
            self.vrl(root.left, height + 1)
