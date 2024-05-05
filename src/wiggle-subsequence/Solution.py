// https://leetcode.com/problems/wiggle-subsequence

class Solution:
    def wiggleMaxLength(self, nums: [int]) -> int:
        if(len(nums) < 2): return len(nums)
        if(len(nums) == 2): return 2 - (nums[0]==nums[1])
        best = 0
        for positive in (False,True):
            last_num = nums[0]
            total = 1
            for n in nums[1:]:
                if(n > last_num and positive or n < last_num and not positive):
                    last_num = n
                    positive = not positive
                    total += 1
                last_num = n
            best = max(best,total)
        return best