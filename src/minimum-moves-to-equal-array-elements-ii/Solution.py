# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        med = sorted(nums)[len(nums)//2]
        return sum(abs(el-med) for el in nums)