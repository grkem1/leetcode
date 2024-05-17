# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pruned_right = ""
        height = 0
        for l in s:
            if(l == '('):
                height += 1
                pruned_right += l
            elif(l == ')'):
                if(height > 0):
                    height -= 1
                    pruned_right += l
            else:
                pruned_right += l
        if(height == 0): return pruned_right
        height = 0
        rs = ""
        for l in pruned_right[::-1]:
            if(l == ')'):
                height += 1
                rs += l
            elif(l == '('):
                if(height > 0):
                    height -= 1
                    rs += l
            else:
                rs += l
        return rs[::-1]