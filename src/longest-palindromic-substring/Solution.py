# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = [0,1]
        for i in range(len(s)):
            j = 1
            while(i-j >= 0 and i+j < len(s)):
                if(s[i-j] == s[i+j]):
                    if(best[1] < 2*j+1):
                        best = [i-j,2*j+1]
                    j += 1
                else:
                    break
        for i in range(len(s)-1):
            if(s[i] != s[i+1]):
                continue
            if(best[1] < 2):
                best = [i,2]
            j = 1
            while(i-j >= 0 and i+j+1 < len(s)):
                if(s[i-j] == s[i+j+1]):
                    if(best[1] < 2*j+2):
                        best = [i-j,2*j+2]
                    j+=1
                else:
                    break
        return s[best[0]:best[0]+best[1]]