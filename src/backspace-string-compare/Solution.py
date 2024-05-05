// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_index = len(s)-1
        t_index = len(t)-1
        s_ignore = 0
        t_ignore = 0
        while(s_index >= 0 or t_index >= 0):
            if(s_index >= 0 and s[s_index] == '#'):
                s_index -= 1
                s_ignore += 1
            elif(t_index >= 0 and t[t_index] == '#'):
                t_index -= 1
                t_ignore += 1
            else:
                if(t_index >= 0 and t_ignore):
                    t_index -= 1
                    t_ignore -= 1
                elif(s_index >= 0 and s_ignore):
                    s_index -= 1
                    s_ignore -= 1
                else:
                    if(s_index < 0 or t_index < 0 or s[s_index] != t[t_index]):
                        return False
                    s_index -= 1
                    t_index -= 1
        return True