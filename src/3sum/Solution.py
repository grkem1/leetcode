// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        threes = []
        prev_nums_i = 10**5+1
        for i in range(len(nums)-2):
            if(nums[i]==prev_nums_i):continue
            prev_nums_i = nums[i]
            j,k = i+1,len(nums)-1
            target = -nums[i]
            while(j<k):
                if(nums[j]+nums[k]>target):
                    k-=1
                    while(k>j and nums[k]==nums[k+1]):k-=1
                elif(nums[j]+nums[k]<target):
                    j+=1
                    while(k>j and nums[j]==nums[j-1]):j+=1
                else:
                    threes.append([nums[i],nums[j],nums[k]])
                    k-=1
                    while(k>j and nums[k]==nums[k+1]):k-=1
                    j+=1
                    while(k>j and nums[j]==nums[j-1]):j+=1
        return threes

