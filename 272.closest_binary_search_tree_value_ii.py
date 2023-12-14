# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:  # noqa
        '''
        Always explore the node with maximum potentiality.
        potentiality: How close the node could be for given interval.
        Time complexity: log(N).

        Improvement
        assumption: values are in Integers

        '''
        Q = []
        Q.append((0, float('-inf'), float('inf'), root))
        candidates = []
        max_diff = abs(root.val - target) + 1
        while Q:
            _, lower_bound, upper_bound, node = heapq.heappop(Q)
            heapq.heappush(candidates, (abs(node.val-target), node.val))
            diff = abs(node.val - target)
            max_diff = max(max_diff, diff)

            if node.right:
                new_lower_bound = node.val + 1
                new_upper_bound = upper_bound
                if new_lower_bound <= target <= new_upper_bound:
                    potentiality = 0
                else:
                    potentiality = min(abs(target-new_lower_bound), abs(target-new_upper_bound))
                if potentiality <= max_diff or len(candidates) < k:
                    heapq.heappush(Q, (potentiality, new_lower_bound, new_upper_bound, node.right))
            if node.left:
                new_lower_bound = lower_bound
                new_upper_bound = node.val - 1
                if new_lower_bound <= target <= new_upper_bound:
                    potentiality = 0
                else:
                    potentiality = min(abs(target-new_lower_bound), abs(target-new_upper_bound))
                if potentiality <= max_diff or len(candidates) < k:
                    heapq.heappush(Q, (potentiality, new_lower_bound, new_upper_bound, node.left))
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(candidates)[1])
        return ret
