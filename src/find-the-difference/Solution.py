# https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = sum(ord(l) for l in s)
        sum_t = sum(ord(l) for l in t)
        return chr(sum_t - sum_s)