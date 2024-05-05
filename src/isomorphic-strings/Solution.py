// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)): return False
        mapping = [None]*128
        rev_map = [None]*128
        for i in range(len(s)):
            if(mapping[ord(s[i])]==t[i] and rev_map[ord(t[i])]==s[i]):
                pass
            elif(mapping[ord(s[i])]==rev_map[ord(t[i])]==None):
                mapping[ord(s[i])]=t[i]
                rev_map[ord(t[i])]=s[i]
            else:
                return False
        return True