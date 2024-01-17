class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.children = [(y, x), ]

    def __len__(self):
        return len(self.children)

    def __hash__(self):
        return hash((self.y, self.x))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:  # noqa
        '''
        space O(mn)
        time amortized cost O(mn)
        '''
        if m == 1 and n == 1:
            return [1]
        y, x = positions[0]
        hashdict = {(y, x): Node(y, x)}
        ret = [1, ]

        for y, x in positions[1:]:
            node_set = set()
            if (y, x) in hashdict:
                ret.append(ret[-1])
                continue

            if (y-1, x) in hashdict:
                node_set.add(hashdict[(y-1, x)])
            if (y+1, x) in hashdict:
                node_set.add(hashdict[(y+1, x)])
            if (y, x-1) in hashdict:
                node_set.add(hashdict[(y, x-1)])
            if (y, x+1) in hashdict:
                node_set.add(hashdict[(y, x+1)])
            if len(node_set) == 0:
                hashdict[(y, x)] = Node(y, x)
                count = ret[-1] + 1
            elif len(node_set) == 1:
                node = next(node_set.__iter__())
                node.children.append((y, x))
                hashdict[(y, x)] = node
                count = ret[-1]
            else:
                # get largest node
                largest_node = max(node_set, key=lambda x: len(x))
                largest_node.children.append((y, x))
                hashdict[(y, x)] = largest_node
                count = ret[-1]
                for node in node_set:
                    if node == largest_node:
                        continue
                    largest_node.children.extend(node.children)
                    count -= 1
                    for y2, x2 in node.children:
                        hashdict[(y2, x2)] = largest_node
            ret.append(count)
        return ret
