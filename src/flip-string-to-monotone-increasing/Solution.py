// https://leetcode.com/problems/flip-string-to-monotone-increasing

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one_cost = 0
        zero_cost = 0
        for l in s:
            if(l == '0'):
                one_cost = min(zero_cost, one_cost + 1)
            else:
                zero_cost += 1
        return min(one_cost,zero_cost)