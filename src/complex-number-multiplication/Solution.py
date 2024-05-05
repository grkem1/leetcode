// https://leetcode.com/problems/complex-number-multiplication

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(s):
            nums = s.split('+') 
            return int(nums[0]),int(nums[1][:-1]) 
        r1,j1 = parse(num1) 
        r2,j2 = parse(num2) 
        r3,j3 = r1*r2-j1*j2,r1*j2+r2*j1 
        return str(r3)+'+'+str(j3)+'i' 