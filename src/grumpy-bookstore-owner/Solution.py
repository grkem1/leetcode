# https://leetcode.com/problems/grumpy-bookstore-owner

class Solution:
    def maxSatisfied(self, customers: [int], grumpy: [int], minutes: int) -> int:
        current = sum(customers[:minutes]) + sum( customers[i] * (1-grumpy[i]) for i in range(minutes, len(customers)) )
        best = current
        for left in range(0, len(customers) - minutes):
            right = left + minutes
            current += ( grumpy[right] * customers[right] - grumpy[left] * customers[left] )
            best = max(best, current)
        return best
