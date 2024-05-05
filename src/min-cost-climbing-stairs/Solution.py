// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Find minimum cumulative cost for each stair, return min of last two
        first, second = cost[0], cost[1]
        for el in cost[2:]:
            el += min(first,second)
            first,second = second,el
        return min(first,second)