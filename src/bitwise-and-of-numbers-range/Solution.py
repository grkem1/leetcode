# https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        temp = 1
        while(temp < right):
            temp *= 2
        while(temp > 0):
            if(left & temp):
                if(right & temp):
                    result += temp
                    temp //= 2
                    continue
                else:
                    print("shouldnt get here")
            else:
                if(right & temp):
                    return result
                else:
                    temp //= 2
                    continue
        return result