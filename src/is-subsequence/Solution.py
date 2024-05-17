# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s) > len(t)):
            return False
        if(len(s) == 0):
            return True
        i = 0
        for letter in t:
            if(letter == s[i]):
                i+=1
                if(i == len(s)):
                    return True
        return False