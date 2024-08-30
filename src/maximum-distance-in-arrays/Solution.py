# https://leetcode.com/problems/maximum-distance-in-arrays

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_ = arrays[0][0]
        max_ = arrays[0][-1]
        best = 0
        for a in arrays[1:]:
            best = max(best, a[-1] - min_, max_ - a[0])
            min_ = min(min_, a[0])
            max_ = max(max_, a[-1])
        return best
