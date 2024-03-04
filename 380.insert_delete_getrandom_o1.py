import random


class RandomizedSet:

    def __init__(self):
        '''
        Implement a list and hashmap to access getRandom in O(1)
        '''
        self.hash_map = {}
        self.array = []
        self.n = 0

    def insert(self, val: int) -> bool:
        if self.hash_map.get(val, None) is None:
            if self.n == len(self.array):
                self.array.append(val)
            else:
                self.array[self.n] = val

            idx = self.n
            self.hash_map[val] = idx

            self.n += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if self.hash_map.get(val, None) is not None:
            src_idx = self.hash_map[val]
            last_idx = self.n - 1
            last_val = self.array[last_idx]
            self.array[src_idx] = last_val
            self.hash_map[last_val] = src_idx
            self.hash_map[val] = None
            self.n -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.array[:self.n])


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
