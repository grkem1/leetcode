# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        s_new = [s[0]]
        for l in s[1:]:
            if(s_new and s_new[-1] == l):
                s_new.pop()
            else:
                s_new.append(l)
        return ''.join(s_new)