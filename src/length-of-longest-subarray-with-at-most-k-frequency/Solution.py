# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = j = 0
        best = 1
        count = defaultdict(int)
        count[nums[0]] = 1
        while(i < len(nums)-1 and j < len(nums)-1):
            j += 1
            count[nums[j]] += 1
            while(count[nums[j]] > k):
                count[nums[i]] -= 1
                i += 1
            best = max(best, j-i+1)
        return best