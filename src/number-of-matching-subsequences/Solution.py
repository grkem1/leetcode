# https://leetcode.com/problems/number-of-matching-subsequences

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c = len(words)
        for w in words:
            i = 0
            for l in w:
                i = s.find(l,i)
                if(i == -1):
                    c-=1
                    break
                i+=1
        return c