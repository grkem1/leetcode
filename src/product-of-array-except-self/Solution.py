# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = functools.reduce(lambda x,y: x*y, nums)
        if(0 in nums):
            if(0 in nums[nums.index(0)+1:]): # second 0?
                return [0]*len(nums)
            return [0]*nums.index(0) + [reduce(lambda x,y:x*y, nums[:nums.index(0)]+nums[nums.index(0)+1:])] + [0]*(len(nums)-nums.index(0)-1)
        ans = []
        for n in nums:
            ans.append(mul//n)
        return ans