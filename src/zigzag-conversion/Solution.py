// https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1): return s
        period = (numRows - 1) * 2
        newStrs = [[] for i in range(numRows)]
        for i,l in enumerate(s):
            row = i % period
            row = min(row, period - row)
            newStrs[row].append(l)
        s = []
        for r in newStrs:
            for l in r:
                s.append(l)
        return "".join(s)