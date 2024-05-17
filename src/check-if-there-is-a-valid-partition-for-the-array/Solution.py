# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n_3 = n_2 = n_1 = False
        def good(i):
            nonlocal nums,n_3,n_2
            if(n_3 and (nums[i]==nums[i-1]==nums[i-2] or nums[i]==nums[i-1]+1 and nums[i-1]==nums[i-2]+1) ):
                return True
            return (n_2 and nums[i]==nums[i-1])
        
        if(len(nums) == 2): return nums[0] == nums[1]
        if(len(nums) == 3): return nums[0] == nums[1] == nums[2] or nums[2] == nums[1]+1 and nums[1] == nums[0]+1
        n_3, n_2, n_1, n_0 = True, False, nums[0] == nums[1], False
        for i in range(2,len(nums)):
            if(n_3 == n_2 == n_1 == False):
                return False
            n_0 = good(i)
            n_3,n_2,n_1 = n_2,n_1,n_0
        return n_0