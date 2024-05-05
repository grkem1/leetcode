// https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        new_s = []
        for l in s:
            if(l != '*'):
                new_s.append(l)
            else:
                new_s.pop()
        return ''.join(new_s)