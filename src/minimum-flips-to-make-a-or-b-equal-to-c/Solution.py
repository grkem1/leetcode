# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        total = 0
        while(c > 0 or a > 0 or b > 0):
            if(c & 1):
                if( (a & 1 | b & 1) == 0):
                    total += 1
            else:
                if(a&1):total+=1
                if(b&1):total+=1
            c = c >> 1
            a = a >> 1
            b = b >> 1
        return total