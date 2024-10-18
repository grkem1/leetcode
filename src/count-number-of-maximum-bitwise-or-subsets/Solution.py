# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets

# Brute force solution. There are at least two better solutions to this problem.
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        best = functools.reduce(lambda x,y: x | y, nums)
        count = 0
        for i in range(1, 2**len(nums)):
            current = 0
            for j in range(len(nums)):
                current |= (i & 2**j != 0) * nums[j]
            count += (current == best)
        return count
