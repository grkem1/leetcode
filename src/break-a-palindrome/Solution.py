// https://leetcode.com/problems/break-a-palindrome

class Solution:
    def breakPalindrome(self, p: str) -> str:
        l = len(p)
        if(l < 2):return ""
        for i in range(l//2):
            if(p[i]!='a'):
                return p[:i]+'a'+p[i+1:]
        return p[:-1]+'b'
#        for i in range(l-1,(l-1)//2,-1):
#            if(p[i]!='z'):
#                return p[:i]+chr(ord(p[i])+1)+p[i+1:]