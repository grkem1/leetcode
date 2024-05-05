// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: [int]) -> int:
        if(len(nums)<2 or nums[0]<nums[-1]):return nums[0]
        upper,lower = len(nums),0
        while(upper > lower):
            i = (upper+lower)//2
            if(nums[i]<nums[i-1]):
                return nums[i]
            else:
                if(nums[i]>nums[0]):
                    lower=i
                else:
                    upper=i
        print("not found")