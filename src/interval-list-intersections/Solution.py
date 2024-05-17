# https://leetcode.com/problems/interval-list-intersections

class Solution:
    def intervalIntersection(self, firstList: [[int]], secondList: [[int]]) -> [[int]]:
        first_starts = [i[0] for i in firstList]
        first_ends   = [i[1] for i in firstList]
        intervalList = []
        def intersect(a,b):
            return [max(a[0],b[0]),min(a[1],b[1])]
        for i in secondList:
            ends_after    = bisect.bisect(first_starts, i[1])
            starts_before = bisect.bisect_left(first_ends, i[0])
            for j in range(starts_before, ends_after):
                intervalList.append(intersect(i,firstList[j]))
        return intervalList
