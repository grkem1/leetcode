# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        el = 0
        for n in nums:
            el ^= n
        return el