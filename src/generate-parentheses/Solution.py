// https://leetcode.com/problems/generate-parentheses

class Solution:
    solns_array = []
    def generateParenthesis(self, n: int) -> [str]:
        def recurse_down(steps_down,steps_up,steps_max,path):
            if(steps_down == steps_max):
                path = path + (steps_down - steps_up) * ")"
                self.solns_array = self.solns_array + [path]
                return
            if(steps_down < steps_max):
                recurse_down(steps_down+1,steps_up,steps_max,path+"(")
            if(steps_up < steps_down):
                recurse_down(steps_down,steps_up+1,steps_max,path+")")
        recurse_down(0,0,n,"")
        return self.solns_array