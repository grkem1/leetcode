# https://leetcode.com/problems/find-the-highest-altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max( 0,max(accumulate(gain)) )