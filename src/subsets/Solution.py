// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        return [[nums[index] for index,mask in map(lambda k:(k,2**k),range(len(nums))) if i&mask] for i in range(2**len(nums))]
