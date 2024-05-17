# https://leetcode.com/problems/repeated-substring-pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        i = 2
        while(l > 1):
            if(l % i == 0):
                if(s == i * s[0:len(s)//i]):
                    return True
                while(l % i == 0):
                    l = l // i
            i += 1
        return False