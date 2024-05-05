// https://leetcode.com/problems/predict-the-winner

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = dict()
        def best(left,right):
            nonlocal memo,nums
            if(left == right): return nums[left]
            if((left,right) in memo):
                return memo[(left,right)]
            res = max(nums[left]-best(left+1,right), nums[right]-best(left,right-1))
            memo[(left,right)] = res
            return res
        return best(0,len(nums)-1) >= 0