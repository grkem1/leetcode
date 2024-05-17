# https://leetcode.com/problems/valid-triangle-number

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]!=0):break
        nums=nums[i:]
        if(len(nums)<3):return 0
        c=0 
        for i1,n1 in enumerate(nums[:-2]):
            for i2 in range(i1+1,len(nums)-1):
                n2=nums[i2]
                i3=bisect.bisect_left(nums,n1+n2)
                c+=i3-i2-1
#                print("n1:",n1," n2:",n2," i3:",i3," c_i2:",c_i2)
        return c
 
