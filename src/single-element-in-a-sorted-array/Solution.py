// https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res