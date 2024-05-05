// https://leetcode.com/problems/find-unique-binary-string

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # convert to number, sort the array, binary search...
        nums = sorted(int(n,2) for n in nums)
        # print(nums)
        if(nums[0] != 0):
            return "0"*len(nums)
        if(nums[-1] != 2**len(nums)-1):
            return "1"*len(nums)
        left, right = 0, len(nums)-1
        mid = (left + right ) // 2
        while(left+2 < right):
            missing_right = (nums[right] - nums[mid]) - (right-mid)
            missing_left = (nums[mid] - nums[left]) - (mid-left)
            if(missing_right > missing_left):
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        # print(left,right,mid)
        missing = nums[mid] + 1 if nums[mid] + 1 != nums[right] else nums[left] + 1
        missing = bin(missing)[2:]
        missing = "0"*(len(nums)-len(missing))+missing
        return missing