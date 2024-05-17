# https://leetcode.com/problems/partition-to-k-equal-sum-subsets

class Solution:
    def canPartitionKSubsets(self, nums: [int], k: int) -> bool:
        total = sum(nums)
        if(total%k != 0):return False
        nums.sort(reverse=True)
        remaining = [total//k]*k
        def insert(num,bucket):
            nonlocal nums,remaining
            if(num == len(nums)):return True
            if(nums[num]>remaining[bucket]):return False
            remaining[bucket]-=nums[num]
            for b in range(k):
                if(insert(num+1,b)):
                    return True
            remaining[bucket]+=nums[num]
            return False
        for b in range(k):
            if(insert(0,b)):
                return True
        return False
