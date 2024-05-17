# https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        nums.sort()
        subsets = set()
        l = len(nums)
        for i in range(2**l):
            ss = []
            for j in range(l):
                if((i>>j) & 1): 
                    ss.append(nums[j])
            subsets.add(tuple(ss))
        return [list(i) for i in subsets]
