// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        right = bisect.bisect(nums,target)
        if(right == 0 or nums[right-1] != target): return [-1,-1]
        return([bisect.bisect_left(nums[:right],target),right-1])