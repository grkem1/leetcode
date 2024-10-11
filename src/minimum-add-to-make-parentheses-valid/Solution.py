# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        level = 0
        needed = 0
        for c in s:
            if(c == ')'):
                if(level == 0):
                    needed += 1
                else:
                    level -= 1
            else:
                level += 1
        return level + needed
