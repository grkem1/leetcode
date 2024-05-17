# https://leetcode.com/problems/reverse-only-letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = [i for i in s]
        i,j = 0,len(s)-1
        while(s[i].isalpha()==False and i < j):i+=1
        while(s[j].isalpha()==False and j > i):j-=1
        while(i < j): 
            s[i],s[j]=s[j],s[i]
            i,j = i+1,j-1
            while(s[i].isalpha()==False):i+=1
            while(s[j].isalpha()==False):j-=1
        return "".join(s)