# https://leetcode.com/problems/power-of-four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n == 0 or n & (n-1)): return False
        root = n
        while(root * root != n and root != 0):
            root = root >> 1
        return root != 0 and (root & (root - 1)) == 0