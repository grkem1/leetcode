# https://leetcode.com/problems/minimum-operations-to-make-array-equal

class Solution:
    def minOperations(self, n: int) -> int:
        return n*(n//2)-(n//2)**2