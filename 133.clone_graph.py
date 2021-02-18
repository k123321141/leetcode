"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node': # noqa
        if node is None:
            return None
        elif len(node.neighbors) == 0:
            return Node(node.val) # noqa
        from collections import deque
        ret = Node(node.val) # noqa

        Q = deque()
        visited = {ret.val: ret}
        Q.append((node, ret))
        while len(Q) > 0:
            src, copy_src = Q.popleft()
            for dst in src.neighbors:
                if dst.val not in visited:
                    copy_dst = Node(dst.val) # noqa
                    visited[dst.val] = copy_dst
                    Q.append((dst, copy_dst))
                else:
                    copy_dst = visited[dst.val]
                copy_src.neighbors.append(copy_dst)
        return ret
