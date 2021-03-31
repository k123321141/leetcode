from functools import cache
from collections import deque


class Node:
    def __init__(self):
        self.val = self.left = self.right = None

    def __repr__(self):
        return f'val: {self.val}, left: {self.left.__repr__()}, right: {self.right.__repr__()}'


class KDTree:
    def __init__(self, arr: List[List[int]]): # noqa
        self.root = self.create_node(arr, use_width=True)
        # print(self.root)

    def find_smaller_than(self, width: int, height: int) -> List[List[int]]: # noqa
        ret = []
        Q = deque()
        Q.append([self.root, True])
        while Q:
            node, use_width = Q.popleft()
            w, h = node.val
            if w < width and h < height:
                ret.append([w, h])
            if use_width:
                if w <= width and node.right:
                    Q.append([node.right, not use_width])
            else:
                if h <= height and node.right:
                    Q.append([node.right, not use_width])
            if node.left:
                Q.append([node.left, not use_width])
        return ret

    def create_node(self, arr, use_width) -> Node:
        if len(arr) == 1:
            node = Node()
            node.val = arr[0]
            return node
        elif len(arr) == 2:
            a, b = arr
            node_a = Node()
            node_a.val = a
            node_b = Node()
            node_b.val = b
            if use_width:
                if a[0] < b[0]:
                    node_b.left = node_a
                else:
                    node_b.right = node_a
            else:
                if a[1] < b[1]:
                    node_b.left = node_a
                else:
                    node_b.right = node_a
            return node_b
        # first layer use width as pivot
        idx = self.find_median(arr, use_width)

        left_arr = []
        right_arr = []
        for i, (w, h) in enumerate(arr):
            if i == idx:
                continue
            if use_width:
                if w < arr[idx][0]:
                    left_arr.append([w, h])
                else:
                    right_arr.append([w, h])
            else:
                if h < arr[idx][1]:
                    left_arr.append([w, h])
                else:
                    right_arr.append([w, h])
        #
        root = Node()
        root.val = arr[idx]
        if len(left_arr) > 0:
            root.left = self.create_node(left_arr, not use_width)
        root.right = self.create_node(right_arr, not use_width)
        return root

    def find_median(self, arr: List[List[int]], use_width: bool) -> int: # noqa
        N = len(arr)
        sorted_arr = sorted(arr, key=lambda x: x[0] if use_width else x[1])
        w, h = sorted_arr[N//2] if N % 2 == 1 else sorted_arr[N//2-1]
        for i in range(len(arr)):
            if use_width:
                if w == arr[i][0]:
                    return i
            else:
                if h == arr[i][1]:
                    return i


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int: # noqa
        if len(envelopes) == 1:
            return 1
        envelopes = list(set([(w, h) for w, h in envelopes]))
        self.tree = KDTree(envelopes)
        for w, h in envelopes:
            c = 0
            # self.tree.find_smaller_than(w, h)
            for a, b in envelopes:
                if a < w and b < h:
                    c += 1
        return 1
        return max([self.dp(w, h) for w, h in envelopes])

    @cache
    def dp(self, width: int, height: int) -> int:
        ret = 1
        for w, h in self.tree.find_smaller_than(width, height):
            ret = max(self.dp(w, h)+1, ret)
        return ret
