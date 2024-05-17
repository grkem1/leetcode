# https://leetcode.com/problems/two-city-scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        preferences = sorted((c[1]-c[0],i) for i,c in enumerate(costs))
        total_cost = 0
        for i in range(len(costs)//2):
            total_cost += costs[preferences[i][1]][1]
        for i in range(len(costs)//2,len(costs)):
            total_cost += costs[preferences[i][1]][0]
        return total_cost