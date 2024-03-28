# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:  # noqa
        self.cache = {}
        left_count = self.count(root.left) if root.left else 0
        while left_count != (k - 1):
            if left_count < k - 1:
                root = root.right
                left_count += 1
                if root.left:
                    left_count += self.count(root.left)
            else:
                root = root.left
                left_count -= 1
                if root.right:
                    left_count -= self.count(root.right)
        return root.val

    def count(self, root) -> int:
        if root is None:
            return 0
        key = id(root)
        if key in self.cache:
            return self.cache[key]
        if root.left is None and root.right is None:
            ret = 1
        else:
            ret = 1
            if root.left:
                ret += self.count(root.left)
            if root.right:
                ret += self.count(root.right)
        self.cache[key] = ret
        return ret
