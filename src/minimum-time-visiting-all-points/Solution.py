// https://leetcode.com/problems/minimum-time-visiting-all-points

class Solution:
    def minTimeToVisitAllPoints(self, points: [[int]]) -> int:
        def dist(a,b):
            return max(abs(a[0]-b[0]),abs(a[1]-b[1]))
        total_dist = 0
        for pair in zip(points,points[1:]):
            total_dist += dist(pair[0],pair[1])
        return total_dist