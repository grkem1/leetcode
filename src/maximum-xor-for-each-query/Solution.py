# https://leetcode.com/problems/maximum-xor-for-each-query

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        goal = (2 ** maximumBit) - 1
        current = 0
        result = []
        for n in nums:
            current ^= n
            result.append(goal ^ current)
        return result[::-1]
