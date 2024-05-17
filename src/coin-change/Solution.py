# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counts = [amount+1]*(amount+1)
        counts[0] = 0
        for i in range(amount+1):
            for c in coins:
                if(c > i):
                    continue
                counts[i] = min(counts[i],counts[i-c]+1)
        return counts[amount] if counts[amount] < amount+1 else -1