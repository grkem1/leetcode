# https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min_index = 0
        min_cum = 10**4
        cum = 0
        for i in range(len(gas)):
            diff = gas[i]-cost[i]
            cum += diff
            if(min_cum > cum):
                min_index = i
                min_cum = cum
        if(cum < 0):
            return -1
        return (min_index + 1)%len(gas)
#        print("gas:", gas)
#        print("cost:", cost)
#        print("diff:", diff)
#        print("cum:", cum)