// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i_unique = 0
        last_count = 1
        last_number = 10**5
        for i,current_number in enumerate(nums):
            if(last_number == current_number):
                last_count += 1
                if(last_count > 2):
                    continue
            else:
                last_count = 1
                last_number = current_number
            nums[i_unique] = current_number
            i_unique += 1
        # print(nums)
        return i_unique