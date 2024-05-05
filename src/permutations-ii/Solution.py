// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        # print(nums)
        def reverse(i):
            nonlocal nums
            nums = nums[:i] + nums[i:][::-1]
        def swap(i,j):
            nonlocal nums
            nums[i],nums[j] = nums[j],nums[i]
        nums.sort()
        perms = []
        perms.append(nums.copy())
        while(True):
            i = len(nums)-2
            while(i > -1 and nums[i+1]<=nums[i]):
                i-=1
            if(i == -1):
                return perms
            j = len(nums)-1
            while(nums[j] <= nums[i]):
                j-=1
            swap(i,j)
            reverse(i+1)
            perms.append(nums.copy())
            # print(perms)