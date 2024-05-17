# https://leetcode.com/problems/broken-calculator

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        step = 0
        while(target > startValue):
            target,mod = divmod(target,2)
            step += 1
            if(mod == 1):
                step += 1
                target += 1
        return step + (startValue - target)