// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell,profit = prices[0],prices[0],0
        for p in prices[1:]:
            if(p < buy):
                buy = p
                sell = p
            elif(p > sell):
                sell = p
                profit = max(profit,sell-buy)
        return profit