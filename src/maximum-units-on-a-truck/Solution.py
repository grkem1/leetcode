# https://leetcode.com/problems/maximum-units-on-a-truck

class Solution:
    def maximumUnits(self, boxTypes: [[int]], truckSize: int) -> int:
        total = 0 
        for b in sorted(boxTypes, key = lambda t: t[1], reverse=True):
            if(truckSize >= b[0]):
                total += b[0]*b[1]
                truckSize -= b[0]
            else:
                total += truckSize * b[1]
                break
        return total
