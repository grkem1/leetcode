# https://leetcode.com/problems/reorganize-string

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = collections.Counter(s)
        commons = c.most_common()
        if(commons[0][1] > len(s)//2 + len(s)%2):
            return ""
        rv = [None]*len(s)
        last = 0
        for common in commons:
            for i in range(common[1]):
                if(last >= len(s)):
                    last = 1
                rv[last] = common[0]
                last += 2
        return "".join(rv)