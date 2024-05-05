// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        current = nums[0]
        best = len(nums) + 1
        if(current >= target): best = j-i+1
        while(True):
            if(current >= target):
                best = min(best, j-i+1)
                if(i < j):
                    current -= nums[i]
                    i += 1
                else:
                    j += 1
                    if(j == len(nums)):break
                    current += nums[j]
            else:
                j += 1
                if(j == len(nums)):break
                current += nums[j]
        return best if best < len(nums)+1 else 0