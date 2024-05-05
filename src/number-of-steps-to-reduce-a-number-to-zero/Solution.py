// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while(num > 1):
            num,mod = divmod(num,2)
            steps += (1 + mod)
        if(num == 1):steps += 1
        return steps