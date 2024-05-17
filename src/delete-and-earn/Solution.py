# https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, nums: [int]) -> int:
        nums_values = collections.defaultdict(int)
        for n in sorted(nums):
            nums_values[n]+=n
        last = -1
        take = 0
        no_take = 0
        for n in nums_values:
            if(last == n-1):
                take,no_take = nums_values[n]+no_take,max(take,no_take)
            else:
                take,no_take = nums_values[n]+max(take,no_take),max(take,no_take)
            last = n
        # print(nums_values)
        return max(take,no_take)