// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = 1
        lis  = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    lis[i]=max(lis[i],lis[j]+1)
                    m=max(m,lis[i])
        # print(lis)
        return m