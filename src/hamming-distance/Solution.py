# https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = x ^ y
        count = 0
        while(dist != 0):
            count += 1
            dist &= dist - 1
        return count