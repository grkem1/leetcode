# https://leetcode.com/problems/maximum-erasure-value

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = r = 0
        s = m = nums[0]
        contains = set([nums[0]])
        while(True):
            r+=1
            if(r == len(nums)):break
            if(nums[r] in contains):
                while(nums[l] != nums[r]):
                    s -= nums[l]
                    contains.remove(nums[l])
                    l += 1
                if(l != r):
                    s -= nums[l]
                    contains.remove(nums[l])
                    l += 1
            s += nums[r]
            contains.add(nums[r])
            m = max(m,s)
        return m