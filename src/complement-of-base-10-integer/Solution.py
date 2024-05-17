# https://leetcode.com/problems/complement-of-base-10-integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        p = 2
        while(n >= p):
            p*=2
        return (p - n - 1)