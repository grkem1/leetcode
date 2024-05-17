# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop

class Solution:
    def finalPrices(self, prices: [int]) -> [int]:
        s = []
        discounted = []
        for i,p in enumerate(prices[::-1]):
            while(len(s) != 0):
                d = s[-1]
                if(d <= p):
                    discounted.append(p-d)
                    break
                s.pop()
            if(len(discounted)==i): # no discount found
                discounted.append(p)
            s.append(p)
        return discounted[::-1]