# https://leetcode.com/problems/maximum-width-ramp

# Note: this is just a quick sub-optimal solution to the problem. This problem
# is a monotonic stack problem, which can also be solved using two pointers.

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        best = 0
        arr = [(nums[0],0)]
        for i in range(1,len(nums)):
            if(nums[i] < arr[0][0]):
                arr = [(nums[i],i)] + arr
            else:
                best = max(best, i - arr[bisect.bisect(arr,(nums[i],i))-1][1])
        return best
