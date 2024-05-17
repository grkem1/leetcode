# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        min_dp = [0] + (len(nums)-1)*[len(nums)]
        for i in range(len(nums)-1):
            for j in range(i+1,min(len(nums),i+nums[i]+1)):
                min_dp[j] = min(min_dp[j], min_dp[i]+1)
        # print(min_dp)
        return min_dp[-1]