# https://leetcode.com/problems/target-sum


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        two_s1 = sum(nums) + target
        s1 = two_s1 // 2
        if s1 * 2 != two_s1:
            return 0

        @functools.cache
        def dfs(i=len(nums) - 1, t=s1):
            nonlocal nums
            if i < 0:
                return (t == 0) + 0
            if t < nums[i]:
                return dfs(i - 1, t)
            return dfs(i - 1, t) + dfs(i - 1, t - nums[i])

        return dfs()
