# https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        letter_count = [0]*26
        for l in s:
            letter_count[ord(l)-97]+=1
        for l in t:
            letter_count[ord(l)-97]-=1
            if(letter_count[ord(l)-97] < 0):
                return False
        return True