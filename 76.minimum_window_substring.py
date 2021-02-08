class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Just like progress bar in youtube video player.
        Maintain 2 index to represent a window, l & r.
        1. Increase r to expand window untill it contains each word in t.
        2. Then decrease l to get smaller window, till it miss any char in t.
        3. Repeat 1 & 2 to scan whole s.

        '''
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        if len(t) == 1:
            return t if t in s else ""
        counter = {}
        target = {}
        for c in t:
            counter[c] = 0
            if c not in target:
                target[c] = 1
            else:
                target[c] += 1
        l = hit = 0
        r = 1
        # window left, window right
        wl, wr = 0, float('inf')
        # init
        if s[0] in counter:
            counter[s[0]] = 1
            if counter[s[0]] == target[s[0]]:
                hit += 1
        while r < len(s):
            # print(' '*r + 'r')
            # print(s)
            # print(' '*l + 'l')
            # print(f'l: {l}, r: {r}, hit: {hit}, counter: {counter}, [{s[l]}, {s[r]}]\n')
            # increase process
            if hit < len(counter):
                if s[r] not in counter:
                    r += 1
                elif counter[s[r]] >= target[s[r]]:
                    counter[s[r]] += 1
                    r += 1
                else:  # counter[s[r]] < target[s[r]]
                    counter[s[r]] += 1
                    if counter[s[r]] == target[s[r]]:
                        hit += 1
                    if hit < len(counter):
                        r += 1

            # decrease process
            else:
                # valid window
                size = r-l+1
                if size < wr-wl+1:
                    wl, wr = l, r
                #
                if s[l] not in counter:
                    l += 1

                elif counter[s[l]] > target[s[l]]:
                    counter[s[l]] -= 1
                    l += 1
                else:  # counter[s[l]] == target[s[l]]
                    counter[s[l]] -= 1
                    hit -= 1
                    l += 1
                    r += 1

        if wr == float('inf'):
            return ""
        else:
            return s[wl:wr+1]
