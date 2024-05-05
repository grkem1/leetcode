// https://leetcode.com/problems/ugly-number

class Solution:
    def isUgly(self, n: int) -> bool:
        if(n < 1): return False
        for pf in (2,3,5):
            while(n % pf == 0): n //= pf
        return n == 1