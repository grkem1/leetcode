// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        if(num == 0): return 0
        n = num % 9
        return n if n > 0 else 9