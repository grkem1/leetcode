# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        best = -1
        current = nums[0] + nums[1]
        for n in nums[2:]:
            if(current > n):
                best = current + n
            current += n
        return best