# https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        w = {'a','e','i','o','u','A','E','I','O','U'}
        count = 0
        for i in range(len(s)//2):
            if(s[i] in w): count+=1
        for i in range(len(s)//2,len(s)):
            if(s[i] in w): count-=1
        return (count==0)