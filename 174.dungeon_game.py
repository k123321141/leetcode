class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:  # noqa

        h = len(dungeon)
        w = len(dungeon[0])

        minium_hp = []
        for row in dungeon:
            minium_hp.append([1]*len(row))
        minium_hp[-1][-1] = max(1, -1 * dungeon[-1][-1] + 1)

        for y in range(h-2, -1, -1):
            minium_hp[y][-1] = max(1, minium_hp[y+1][-1] - dungeon[y][-1])

        for x in range(w-2, -1, -1):
            minium_hp[-1][x] = max(1, minium_hp[-1][x+1] - dungeon[-1][x])

        for y in range(h-2, -1, -1):
            for x in range(w-2, -1, -1):
                minium_hp[y][x] = min(minium_hp[y+1][x], minium_hp[y][x+1]) - dungeon[y][x]
                minium_hp[y][x] = max(1, minium_hp[y][x])

        return minium_hp[0][0]
