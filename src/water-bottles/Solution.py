# https://leetcode.com/problems/water-bottles

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        full = numBottles
        empty = 0
        while (full + empty >= numExchange):
            drunk += full
            full, empty = divmod(full + empty, numExchange)
        return drunk + full
