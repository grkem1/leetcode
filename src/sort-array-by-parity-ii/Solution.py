# https://leetcode.com/problems/sort-array-by-parity-ii

class Solution:
    def sortArrayByParityII(self, nums: [int]) -> [int]:
        if(len(nums)>1):
            index_odd = []
            for i in range(0,len(nums),2):
                if(nums[i]&1 == 1): 
                    index_odd.append(i)
            j=0 
            for i in range(1,len(nums),2):
                if(nums[i]&1 == 0): 
                    nums[index_odd[j]],nums[i] = nums[i],nums[index_odd[j]]
                    j+=1
        return nums
