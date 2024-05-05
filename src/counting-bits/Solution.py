// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        rv = [None] * (n+1)
        rv[0] = 0
        i = 1
        while(i <= n):
            rv[i] = 1
            for j in range(i+1,min(2*i,n+1)):
                rv[j] = rv[j-i] + 1
            i *= 2
        return rv