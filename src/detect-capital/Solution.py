# https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(len(word) < 2): return True
        if(word[1].isupper()):
            if(word[0].islower()): return False
            return all(s.isupper() for s in word[1:])
        else:
            return all(s.islower() for s in word[1:])