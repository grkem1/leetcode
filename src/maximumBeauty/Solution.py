# https://leetcode.com/problems/maximumBeauty


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = j = 0
        best = 1
        while i <= j < len(nums):
            if nums[j] - nums[i] <= 2 * k:
                best = max(best, j - i + 1)
                j += 1
            else:
                i += 1
        return best
