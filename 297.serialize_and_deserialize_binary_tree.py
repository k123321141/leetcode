# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        O(2N)
        """
        if root is None:
            return ''
        stack = deque()
        s = ''
        stack.append(root)
        while stack:
            node = stack.pop()
            if node is None:
                s += 'x,'
                continue
            s += f'{node.val},'
            if node.right:
                stack.append(node.right)
            else:
                stack.append(None)
            if node.left:
                stack.append(node.left)
            else:
                stack.append(None)
        # print(s)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        O(N)
        """
        if len(data) == 0:
            return None
        val_str, i = self._next(data, 0)
        root = TreeNode(int(val_str))  # noqa
        stack = deque()
        stack.append((root, False))
        stack.append((root, True))
        while stack:
            node, is_left = stack.pop()
            val_str, i = self._next(data, i)
            if val_str == 'x':
                continue
            else:
                child = TreeNode(int(val_str))  # noqa
                if is_left:
                    node.left = child
                else:
                    node.right = child
                stack.append((child, False))
                stack.append((child, True))
        return root

    def _next(self, s: str, idx: int):
        start = idx
        end = idx + 1
        while s[end] != ',':
            end += 1
        return s[start:end], end + 1
