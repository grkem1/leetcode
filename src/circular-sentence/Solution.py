# https://leetcode.com/problems/circular-sentence

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        return all(s[i][0] == s[i-1][-1] for i in range(len(s)))
