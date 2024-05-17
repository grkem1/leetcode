# https://leetcode.com/problems/combination-sum-iv

class Solution:
    dp = None
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.dp = [1] + [-1 for i in range(target)]
        def recursion(nums,target):
            if(self.dp[target] != -1): return self.dp[target]
            self.dp[target] = 0
            for num in nums:
                # print(num,target)
                if(num > target):break
                self.dp[target] += recursion(nums,target-num)
            return self.dp[target]
        a = recursion(nums,target)
        # print(self.dp)
        return a
