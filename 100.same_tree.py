from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: # noqa
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        elif p.val != q.val:
            return False

        stk_1 = deque([p])
        stk_2 = deque([q])

        while len(stk_1):
            p = stk_1.pop()
            q = stk_2.pop()
            if p.val != q.val:
                return False
            else:
                if p.left is not None:
                    if q.left is not None:
                        stk_1.append(p.left)
                        stk_2.append(q.left)
                    else:
                        return False
                elif q.left is not None:
                    return False
                if p.right is not None:
                    if q.right is not None:

                        stk_1.append(p.right)
                        stk_2.append(q.right)
                    else:
                        return False
                elif q.right is not None:
                    return False
        return True

