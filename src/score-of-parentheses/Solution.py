# https://leetcode.com/problems/score-of-parentheses

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        value = [0]
        for p in s:
            # print(value)
            if(p == '('):
                value.append(0)
            else:
                val = value.pop()
                value[-1] += 2*val or 1
        return value[0]