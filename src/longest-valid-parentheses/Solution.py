// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        possible_starts = [-1]*(len(s)+1)
        level = 0
        for index,c in enumerate(s):
            if(c == '('):
                level += 1
                if(possible_starts[level] == -1):
                    possible_starts[level] = index
            else:
                if(possible_starts[level] != -1):
                    max_len = max(max_len,index-possible_starts[level]+1)
                if(possible_starts[level+1] != -1):
                    possible_starts[level+1] = -1
                level -= 1
        return max_len