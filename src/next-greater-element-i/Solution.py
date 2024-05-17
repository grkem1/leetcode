# https://leetcode.com/problems/next-greater-element-i

class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        s,d = [],{}
        for n in nums2[::-1]:
            while(s and s[-1]<n):
                s.pop()
            if(s):
                d[n] = s[-1]
            s.append(n)
        return [d.get(n,-1) for n in nums1]