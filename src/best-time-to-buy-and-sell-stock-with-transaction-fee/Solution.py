// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if(len(prices) < 2): return 0
        cash = 0
        hold = -prices[0]
        for i in range(1,len(prices)):
            cash = max(cash,hold+prices[i]-fee)
            hold = max(hold,cash-prices[i])
        return cash