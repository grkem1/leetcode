# https://leetcode.com/problems/minimum-time-difference

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times = list(sorted(int(t.split(":")[0])*60 + int(t.split(":")[1]) for t in timePoints))
        best = 1440 - times[-1] + times[0]
        for i in range(1, len(times)):
            best = min(best, times[i] - times[i-1])

        return best
