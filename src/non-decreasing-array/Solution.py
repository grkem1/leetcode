// https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def isSorted2(n:[int]):
            return (all((n[i] <= n[i+1]) for i in range(len(n)-1)))
        for i in range(len(nums)-1):
            if(nums[i] > nums[i+1]):
                return( ( (nums[i-1] if i > 0 else -100000) <= nums[i+1] and isSorted2(nums[i+1:])) or (nums[i] <= (nums[i+2] if i < len(nums)-2 else 100000) and isSorted2(nums[i+2:])) )
        return True