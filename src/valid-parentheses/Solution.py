// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        pars = "([{)]}"
        left = []
        for char in s:
            i = pars.find(char)
            if(i < 3):
                left.append(i)
            elif(len(left)==0 or left.pop() + 3 != i):
                return False
        return len(left) == 0