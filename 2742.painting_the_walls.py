class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None
        self.head_skip = False


def S(i: int):
    return 501 + i


def remove(node: Node):
    pre = node.pre
    if pre:
        pre.next = node.next
    if node.next:
        node.next.pre = pre


def insert_node(n_pre: Node, node: Node, n_next: Node):
    if n_pre:
        n_pre.next = node
    if n_next:
        n_next.pre = node


def is_last_node(node: Node) -> bool:
    return node.next is None


def head_str(node: Node) -> str:
    arr = []
    if node is None:
        return 'Null'
    while node:
        if node.head_skip:
            node = node.next
            continue
        arr.append(str(node.val))
        node = node.next
    return ' -> '.join(arr)


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:  # noqa
        # init the linked list
        self.head = Node(0)
        self.cost = cost
        self.time = time
        from collections import deque
        self.stk = deque()
        pre = self.head
        for i in range(1, len(cost)):
            node = Node(i)
            node.pre = pre
            pre.next = node
            pre = node

        self.cache = {}
        print('time', time)
        print('cost', cost)
        return self.dfs(0, 0)

    def dfs(self, paid_time, path_sum):
        if path_sum in self.cache:
            cached_time, cached_cost = self.cache[path_sum]
            if paid_time <= cached_time:
                return cached_cost

        if self.head.head_skip and self.head.next is None:
            return 0
        node = self.head
        min_cost = float('inf')
        while node:
            if node.head_skip:
                node = node.next
                continue
            i = node.val
            cost = self.cost[i]
            time = self.time[i]
            s = S(i)

            n_pre = node.pre
            n_next = node.next

            if node == self.head:
                node.head_skip = True
            else:
                remove(node)

            print(f'index: {i}, list: {head_str(self.head)}')
            # pick free worker
            if paid_time >= time or (is_last_node(node) and paid_time > 0):
                print(f'index: {i}, list: {head_str(self.head)}, free')
                min_cost = min(min_cost, self.dfs(paid_time - time, path_sum + s))

            # pick paid worker
            print(f'index: {i}, list: {head_str(self.head)}, paid')
            min_cost = min(min_cost, self.dfs(paid_time + time, path_sum + s) + cost)

            # skip node
            print(f'index: {i}, list: {head_str(self.head)}, skip')
            min_cost = min(min_cost, self.dfs(paid_time + time, path_sum + s) + cost)

            #
            insert_node(n_pre, node, n_next)
            node = node.next
        print(f'index: {i}, list: {head_str(self.head)}, ret: {min_cost}')
        self.cache[path_sum] = (paid_time, min_cost)
        return min_cost
