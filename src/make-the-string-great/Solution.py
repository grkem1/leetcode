// https://leetcode.com/problems/make-the-string-great

class Solution:
    def makeGood(self, s: str) -> str:
        s_new = [s[0]]
        for i,l in enumerate(s[1:]):
            if(len(s_new) > 0):
                l_swapped = l.swapcase()
                if(l_swapped == s_new[-1]):
                    s_new.pop()
                    continue
            s_new.append(l)
        return ''.join(s_new)