# https://leetcode.com/problems/next-permutation

class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i,j): # i and j inclusive
            nonlocal nums
            while(i < j):
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
        def swap(i,j):
            nonlocal nums
            # print("swapped index {},{}".format(i,j))
            # print("swapped values {},{}".format(nums[i],nums[j]))
            nums[i],nums[j] = nums[j],nums[i]
        def nP(i): # if next permutation is available in nums[i::] apply it and return True
            nonlocal nums
            if(i == len(nums)-1):
                return False # can not do anything
            if(nP(i+1)):
                return True # no need to do anything, next recursion does it already
            if(nums[i] >= nums[i+1]):
                return False # can not do anything, already reverse sorted, no next perm
            for j in range(len(nums)-1,i,-1): # linear search, could be optimized
                if(nums[i] < nums[j]):
                    swap(i,j)
                    break
            # j = bisect.bisect_left(nums[i+1:][::-1],nums[i])
            reverse(i+1,len(nums)-1)
            return True
        np_exists = nP(0)
        if(not np_exists):
            reverse(0,len(nums)-1)