from typing import Tuple, Set, List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: # noqa
        '''
        DP recusive. 76%
        Use the element in candidates, or remove it.
        '''
        # ret = self.foo(candidates, target, {})
        return list([list(t) for t in self.foo(sorted(candidates), target, {})])

    def foo(self, candidates: List[int], target: int, cache: dict) -> Set[Tuple[int]]:
        if len(candidates) == 0 or target == 0:
            return set()
        key = tuple(candidates) + (target, )
        if key in cache:
            return cache[key]
        else:
            first = candidates[0]
            if first > target:
                return set()
            else:
                ret = set()
                if first == target:
                    ret = set()
                    ret.add((first, ))
                else:
                    for t in self.foo(candidates, target-first, cache):
                        ret.add((first, ) + t)
                    for t in self.foo(candidates[1:], target, cache):
                        ret.add(t)
                cache[key] = ret
                return ret
