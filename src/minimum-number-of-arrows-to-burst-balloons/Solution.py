# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        total = 0
        points.sort()
        first = 0
        while(first < len(points)):
            end = points[first][1]
            last = first + 1
            while(last < len(points) and points[last][0] <= end):
                end = min(end, points[last][1])
                last += 1
            total += 1
            first = last
        return total