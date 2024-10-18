# https://leetcode.com/problems/maximum-swap

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        best = sorted(num, reverse=True)
        for i in range(len(num)):
            if(num[i] != best[i]):
                highest = i
                for j in range(i+1, len(num)):
                    if(num[j] >= num[highest]):
                        highest = j
                num[i], num[highest] = num[highest], num[i]
                break
        return int(''.join(num))
