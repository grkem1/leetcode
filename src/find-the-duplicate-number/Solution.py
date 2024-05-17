# https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        last = 0
        for n in sorted(nums):
            if(n == last):
                return n
            last = n