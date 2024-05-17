# https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if(len(intervals) == 0): return [newInterval]
        # i = bisect.bisect_left(intervals,newInterval)
        # if(i == len(intervals)): i -= 1
        # j = i
        # while(j > -1 and intervals[j][1] >= newInterval[0]):
        #     j -= 1
        # j += 1
        # if(j == len(intervals)): j -= 1
        # k = i
        # while(k < len(intervals) and intervals[k][0] <= newInterval[1]):
        #     k += 1
        # k -= 1
        # if(k < 0): k += 1
        # mergedInterval = [min(intervals[j][0],newInterval[0]),max(intervals[k][1],newInterval[1])]
        # if(mergedInterval[0] > intervals[j][1]): j+= 1
        # if(mergedInterval[1] >= intervals[k][0]): k+= 1
        # return intervals[:j] + [mergedInterval] + intervals[k:]
        bisect.insort(intervals,newInterval)
        i = 1
        while(i < len(intervals)):
            if(intervals[i][0] <= intervals[i-1][1]):
                intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])
                intervals.pop(i)
            else: i += 1
        return intervals