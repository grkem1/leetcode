// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if(k == 0):
            return nums
        temp = nums[len(nums)-k:].copy()
        for i in range(len(nums)-k-1,-1,-1):
            nums[i+k] = nums[i]
        for i,t in enumerate(temp):
            nums[i] = t