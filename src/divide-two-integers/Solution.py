# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self,dividend: int,divisor: int)->int:
        neg = ( (dividend < 0) ^ (divisor < 0) )
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        for i in range(31,-1,-1):
            if(dividend >= (divisor << i) ):
                dividend -= (divisor << i)
                result += 1 << i
        result = -result if neg else result
        result = min(result,(1<<31)-1)
        result = max(result,-(1<<31))
        return result
        