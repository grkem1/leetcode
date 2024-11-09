# https://leetcode.com/problems/minimum-array-end

# this problem is tricky, we are counting starting from x until nth number,
# each number in the sequence having the bits that correspond to x set. Only
# dimensions that we can manipulate are the ones that are not set in x.

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        n -= 1
        i = 0
        while(n > 0):
            while((2 ** i) & result):
                i += 1
            result += (2 ** i) * (n & 1)
            n //= 2
            i += 1
        return result
