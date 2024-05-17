# https://leetcode.com/problems/array-nesting

class Solution:
    def arrayNesting(self, nums: [int]) -> int:
        seen = [False]*len(nums)
        m = 1 
        for i in range(len(nums)):
            if(seen[i]):continue
            seen[i]=True
            current_set = set([i])
            while(nums[i] not in current_set):
                current_set.add(nums[i])
                i = nums[i]
                seen[i]=True
            m = max(m,len(current_set))
        return m
