# https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-el for el in nums]
        heapq.heapify(nums)
        score = 0
        for i in range(k):
            score -= nums[0]
            heapq.heapreplace(nums, math.floor(nums[0]/3))
        return score
