# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
       # def isnumber(st):
       #     return (st[0] in ('-','+') and st[1:].isdecimal() or st.isdecimal())
       # return max(-2**31,min(2**32-1,int([n for n in s.split() if isnumber(n)][0])))
        i = 0
        while(i < len(s) and s[i] == ' '):
            i+=1
        if(i == len(s)):return 0
        j = [i,i+1][s[i] in ('-','+')]
        while(j < len(s) and s[j].isdecimal()):
            j+=1
        if(s[i] in ('-','+') and j == i+1 or i==j):
            return 0
        # print(s[i:j])
        return min(2**31-1,max(-2**31,int(s[i:j])))