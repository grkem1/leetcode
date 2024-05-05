// https://leetcode.com/problems/calculate-money-in-leetcode-bank

class Solution:
    def totalMoney(self, n: int) -> int:
        week, day = divmod(n,7)
        total = ( (3+week)*(4+week)//2 - 6 )*7
        for i in range(1+week,1+week+day):
            total += i
        return total