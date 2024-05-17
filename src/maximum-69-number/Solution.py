# https://leetcode.com/problems/maximum-69-number

class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        i = -1
        i_ = 0
        while(temp > 0):
            temp,rem = divmod(temp,10)
            if(rem == 6): i = i_
            i_ += 1
        if(i > -1): num += 3 * (10**i)
        return num