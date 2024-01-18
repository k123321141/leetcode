class CustomList(list):
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return id(self) == id(other)


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:  # noqa
        '''
        space O(mn)
        time amortized cost O(mn)
        '''
        if m == 1 and n == 1:
            return [1]
        y, x = positions[0]
        hashdict = {(y, x): CustomList([(y, x), ])}
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
                hashdict[(y, x)] = CustomList([(y, x), ])
                count = ret[-1] + 1
            elif len(node_set) == 1:
                largest_list = next(node_set.__iter__())
                largest_list.append((y, x))
                hashdict[(y, x)] = largest_list
                count = ret[-1]
            else:
                # get largest node
                largest_list = max(node_set, key=lambda x: len(x))
                largest_list.append((y, x))
                hashdict[(y, x)] = largest_list
                count = ret[-1]
                for other in node_set:
                    if other == largest_list:
                        continue
                    count -= 1
                    for y2, x2 in other:
                        hashdict[(y2, x2)] = largest_list
                    largest_list += other
            ret.append(count)
        return ret
