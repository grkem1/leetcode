# https://leetcode.com/problems/mirror-reflection

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p,q)
        p = p // g
        q = q // g
        p = p % 2
        q = q % 2
        if(p == 1 and q == 0):
            return 0
        elif(p == 1 and q == 1):
            return 1
        elif(p == 0 and q == 1):
            return 2
        else:
            return -1