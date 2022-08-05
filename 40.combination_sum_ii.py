class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        DP recusive. 76%
        Use the element in candidates, or remove it.
        '''
        # ret = self.foo(candidates, target, {})
        return [list(t) for t in self.foo(tuple(sorted(candidates)), target)]

    @lru_cache
    def foo(self, candidates: Tuple[int], target: int) -> Set[Tuple[int]]:

        if len(candidates) == 0 or target == 0:
            return set()
        first = candidates[0]
        if first > target:
            return set()
        else:
            ret = set()
            if first == target:
                ret = set()
                ret.add((first, ))
            else:
                for t in self.foo(candidates, target-first):
                    ret.add((first, ) + t)
                for t in self.foo(candidates[1:], target):
                    ret.add(t)
            return ret
