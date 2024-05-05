// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        current_sum = max_sum = nums[0]
        refresh = current_sum < 0
        for i in range(1,len(nums)):
            if(refresh):
                current_sum = nums[i]
                refresh = False
            else:
                current_sum = current_sum + nums[i]
            if(current_sum < 0):
                refresh = True
            if(current_sum > max_sum):
                max_sum = current_sum
        return max_sum