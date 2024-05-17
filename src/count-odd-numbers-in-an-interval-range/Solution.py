# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low += (1-low % 2)
        high -= (1-high % 2)
        return (high - low)//2 + 1