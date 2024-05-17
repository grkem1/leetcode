# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        best = 0
        for i in range(len(nums)//2):
            best = max(best,nums[i]+nums[-i-1])
        return best