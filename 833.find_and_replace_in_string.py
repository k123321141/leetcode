def counting_sort(collection, coll_min, coll_max):
    coll_len = len(collection)

    # create the counting array
    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    # count how much a number appears in the collection
    for number in collection:
        counting_arr[number - coll_min] += 1

    # sum each position with it's predecessors. now, counting_arr[i] tells
    # us how many elements <= i has in the collection
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    # create the output collection
    ordered = [0] * coll_len

    # place the elements in the output, respecting the original order (stable
    # sort) from end to begin, updating counting_arr
    for i in reversed(range(0, coll_len)):
        ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1

    return ordered


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:  # noqa
        '''
        O(n)
        '''
        idx_dict = {idx: i for i, idx in enumerate(indices)}
        sorted_indices = counting_sort(indices, 0, len(s))
        # sorted_idx_list = sorted(range(len(indices)), key=lambda i: indices[i])
        ret = []
        cursor = 0
        for idx in sorted_indices:
            i = idx_dict[idx]
            src = sources[i]
            dst = targets[i]
            if s[idx: idx+len(src)] == src:
                ret.append(s[cursor:idx])
                ret.append(dst)
            else:
                ret.append(s[cursor:idx+len(src)])
            cursor = idx+len(src)
        if cursor < len(s):
            ret.append(s[cursor:])
        return ''.join(ret)
