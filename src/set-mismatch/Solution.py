// https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        toplam = 0
        returnarray = [0,0]
        for i in range(len(nums)-1):
            toplam = toplam + nums[i]
            if(nums[i] == nums[i+1]):
                returnarray[0] = nums[i]
        toplam = toplam + nums[-1]
        toplam_original = len(nums) * (len(nums) + 1) // 2
        returnarray[1] = toplam_original - toplam + returnarray[0]
        return returnarray