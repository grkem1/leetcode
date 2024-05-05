// https://leetcode.com/problems/arranging-coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        n = 2*n
        r = floor(n**0.5)
        while(r**2+r > n):
            r-=1
        return r