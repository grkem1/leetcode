# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort()
        new_intervals = []
        last_interval_end = -1
        for i in intervals:
            if(i[0]>last_interval_end):
                new_intervals.append(i)
            else:
                new_intervals[-1][1] = max(new_intervals[-1][1],i[1])
            last_interval_end = new_intervals[-1][1]
        return new_intervals
