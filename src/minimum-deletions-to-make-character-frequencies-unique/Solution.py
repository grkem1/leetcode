# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution:
    def minDeletions(self, s: str) -> int:
        letters = collections.Counter(s)
        frequencies = sorted(letters.values())
        total = 0 
        for i in range(len(frequencies)-2,-1,-1):
            if(frequencies[i] >= frequencies[i+1]):
                new_f = max(0,frequencies[i+1]-1)
                total += frequencies[i] - new_f
                frequencies[i] = new_f
        return total