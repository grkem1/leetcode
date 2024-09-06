# https://leetcode.com/problems/count-integers-with-even-digit-sum

class Solution:
    def countEven(self, num: int) -> int:
        def ds(i):
            total = 0
            while(i > 0):
                total += i % 10
                i //= 10
            return total

        return ( num - ds(num) % 2 ) // 2
