// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 0): return 0
        a = int(10**(log(x,10)/2))
        if((a+1)**2 > x): return a
        else: return a+1