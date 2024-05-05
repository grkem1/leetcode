// https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        letters = set()
        total = 1
        for l in s:
            if(l in letters):
                total += 1
                letters = set()
                letters.add(l)
            else:
                letters.add(l)
        return total