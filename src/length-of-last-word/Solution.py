// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(" ")
        if(len(s) == 0):return 0
        return len(s.split(" ")[-1])
        