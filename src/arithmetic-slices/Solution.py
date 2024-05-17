# https://leetcode.com/problems/arithmetic-slices

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if(len(nums) < 3): return 0
        combo = 2
        diff  = nums[1]-nums[0]
        count = 0
        last  = nums[1]
        for num in nums[2:]:
            if(num - last == diff):
                combo += 1
                count += combo - 2
            else:
                diff = num - last
                combo = 2
            last  = num
        return count