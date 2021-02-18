from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    The first element from preorder will be root, the sub array brfore this element in in-order will be left tree.

    in-order : 4 2 5 6 1 8 7 9 3
    pre-order: 1 2 4 5 6 3 7 8 9

    [4 2 5 6] will be left tree.

    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode: # noqa
        # recursive version, 66%
        '''
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            val = preorder[0]
            return TreeNode(val)  # noqa
        else:
            val = preorder[0]
            node = TreeNode(val)  # noqa

            idx = inorder.index(val)
            node.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
            node.right = self.buildTree(preorder[1+idx:], inorder[1+idx:])
            return node
        '''
        if len(preorder) == 0:
            return None
        # interative version 85%
        Q = deque()
        root = TreeNode('root')  # noqa
        Q.append((root, True, 0, 0, len(preorder)))
        idx_dict = {n: idx for idx, n in enumerate(inorder)}
        while len(Q) > 0:
            root_ptr, is_left_child, pre_left, in_left, sub_len = Q.pop()
            if sub_len == 0:
                if is_left_child:
                    root_ptr.left = None
                else:
                    root_ptr.right = None
            elif sub_len == 1:
                val = preorder[pre_left]
                node = TreeNode(val)  # noqa
                if is_left_child:
                    root_ptr.left = node
                else:
                    root_ptr.right = node
            else:
                val = preorder[pre_left]
                node = TreeNode(val)  # noqa
                if is_left_child:
                    root_ptr.left = node
                else:
                    root_ptr.right = node

                split_idx = idx_dict[val]
                next_sub_len = split_idx - in_left
                if next_sub_len == 0:
                    pass
                elif next_sub_len == 1:
                    node.left = TreeNode(val=preorder[1+pre_left])  # noqa
                else:
                    Q.append((node, True, 1+pre_left, in_left, next_sub_len))
                if sub_len-next_sub_len-1 == 0:
                    pass
                elif sub_len-next_sub_len-1 == 1:
                    node.right = TreeNode(val=preorder[1+pre_left+next_sub_len])  # noqa
                else:
                    Q.append((node, False, 1+pre_left+next_sub_len, 1+in_left+next_sub_len, sub_len-next_sub_len-1))
        return root.left
