class Node:
    def __init__(self, val, idx=None):
        self.val = val
        self.idx = idx
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.val}.{self.idx}'

    def __hash__(self):
        return hash(self.val * 100007 + self.idx)

    def __eq__(self, other):
        return self.val == other.val and self.idx == other.idx


class RandomizedCollection:

    def __init__(self):
        '''
        Implement a list and 1 hashmap and a double linkedlist to access getRandom in O(1)
        5%
        '''
        self.hash_map = {}
        self.array = []
        self.n = 0

    def insert(self, val: int) -> bool:
        idx = self.n
        node = Node(val, idx)

        if self.n == len(self.array):
            self.array.append(node)
        else:
            self.array[self.n] = node

        self.n += 1
        pre_node = self.hash_map.get(val, None)
        node.prev = pre_node
        if pre_node:
            pre_node.next = node

        ret = pre_node is None
        self.hash_map[val] = node
        return ret

    def remove(self, val: int) -> bool:
        if self.hash_map.get(val, None) is not None:
            node = self.hash_map[val]

            # swap
            last_idx = self.n - 1
            last_node = self.array[last_idx]
            last_val = last_node.val

            self.array[node.idx] = last_node
            last_node.idx = node.idx
            self.hash_map[last_val] = last_node

            self.n -= 1
            # prev
            if node.prev:
                self.hash_map[val] = node.prev
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
            # next
            elif node.next:
                self.hash_map[val] = node.next
                node.next.prev = node.prev
                if node.prev:
                    node.prev.next = node.next
            #
            else:
                self.hash_map[val] = None

            return True

        else:
            return False

    def getRandom(self) -> int:
        idx = random.randint(0, self.n - 1)  # noqa
        return self.array[idx].val


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
