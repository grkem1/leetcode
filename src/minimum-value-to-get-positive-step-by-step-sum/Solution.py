// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        least = nums[0]
        cum = least
        for n in nums[1:]:
            cum += n
            least = min(least,cum)
        return max(1,1-least)