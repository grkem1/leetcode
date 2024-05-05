// https://leetcode.com/problems/number-of-zero-filled-subarrays

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        zeros = 0
        for i,n in enumerate(nums):
            if(n != 0):
                total += zeros * (zeros + 1) // 2
                zeros = 0
            else:
                zeros += 1
        total += zeros * (zeros + 1) // 2
        return total