// https://leetcode.com/problems/time-needed-to-buy-tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        i = 0
        while(True):
            if(tickets[i] == 0):
                i = (i + 1) % len(tickets)
                continue
            tickets[i] -= 1
            total += 1
            if(tickets[i] == 0 and i == k):
                return total
            i = (i + 1) % len(tickets)