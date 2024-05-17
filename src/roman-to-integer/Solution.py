# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        char_value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        last = 0
        total = 0
        for c in s[::-1]:
            val = char_value[c]
            if(val >= last):
                total += val
            else:
                total -= val
            last = val
        return total