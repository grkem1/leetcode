// https://leetcode.com/problems/teemo-attacking

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        begin = -1
        end = -2
        for i,t in enumerate(timeSeries):
            if(end >= t):
                end = t + duration - 1
            else:
                total += end - begin + 1
                begin = t
                end = t + duration - 1
        total += end - begin + 1
        return total