# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        r_list = [i for i in range(1,nums[0])]
        for start,end in zip(nums,nums[1:]):
            r_list += [i for i in range(start+1,end)]
        r_list += [i for i in range(nums[-1]+1,len(nums)+1)]
        return r_list