// https://leetcode.com/problems/remove-covered-intervals

class Solution:
    def removeCoveredIntervals(self, intervals: [[int]]) -> int:
        intervals.sort(key = lambda k:(k[0],-k[1]))
        last = intervals[0][1]
        counter = 1
        for i in intervals[1:]:
            if(i[1] <= last):
                continue
            counter += 1
            last = i[1]
        return counter