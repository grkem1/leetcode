# https://leetcode.com/problems/guess-number-higher-or-lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high,low = n,1
        g = (n+1)//2
        res = guess(g)
        while(res != 0):
            if(res > 0):
                low = g+1
            else:
                high = g-1
            g = (high+low)//2
            res = guess(g)
        return g