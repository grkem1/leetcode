// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) == 1):
            return [nums]
        # res = []
        # for i in self.permute(nums[:-1:]):
        #     res = res + list(i[:j] + [nums[-1]] + i[j:] for j in range(len(nums)-1,-1,-1))
        res = [i[:j] + [nums[-1]] + i[j:] for j in range(len(nums)-1,-1,-1) for i in self.permute(nums[:-1:])]
        return res