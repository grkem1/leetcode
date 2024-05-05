// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1): return 1
        prev, prev2 = 2,1
        for i in range(n-2):
            prev,prev2 = prev2+prev,prev
        return prev