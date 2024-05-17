# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        for i in range(m-1,-1,-1):
            nums1[i+n] = nums1[i]
        nums1_i = n 
        nums2_i = 0 
        nums1.append(10**9+1)
        nums2.append(10**9+1)
        for i in range(m+n):
            if(nums1[nums1_i] < nums2[nums2_i]):
                nums1[i] = nums1[nums1_i]
                nums1_i += 1
            else:
                nums1[i] = nums2[nums2_i]
                nums2_i += 1
        nums1.pop()
        return nums1