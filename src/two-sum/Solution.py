# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums = list(zip(nums,range(len(nums))))
#        print(nums)
        nums.sort()
#        print(nums)
        i,j = 0,len(nums)-1
        while(True):
            s = nums[i][0]+nums[j][0]
            if(s > target):
                j-=1
            elif(s < target):
                i+=1
            else:
                return [nums[i][1],nums[j][1]]