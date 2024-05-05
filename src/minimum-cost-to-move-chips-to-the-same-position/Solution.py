// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd,even = 0,0
        for p in position:
            if(p % 2 == 0):
                even += 1
            else:
                odd += 1
        return min(odd,even)