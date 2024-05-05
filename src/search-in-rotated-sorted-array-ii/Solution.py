// https://leetcode.com/problems/search-in-rotated-sorted-array-ii

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return target in nums
        # def find_in_sorted(nums,target):
        #     i,j = 0,len(nums)-1
        #     while(i <= j):
        #         mid = (i + j) // 2
        #         if(target > nums[mid]):
        #             i = mid + 1
        #         elif(target < nums[mid]):
        #             j = mid - 1
        #         else:
        #             return mid
        #     return -1
        # def find_rotation(nums):
        #     largest_index = len(nums) - 1
        #     i,j = 0,len(nums) - 1
        #     if(nums[i] < nums[j]):
        #         return 0
        #     while(i <= j):
        #         largest = nums[largest_index]
        #         mid = (i + j) // 2
        #         if(nums[mid] > largest):
        #             largest_index = mid
        #             i = mid + 1
        #         elif(nums[mid] == largest):
        #             largest_index = mid
        #             j = mid - 1
        #         else:
        #             j = mid - 1
        #     return largest_index + 1
        # rotation = find_rotation(nums)
        # index = find_in_sorted(nums[:rotation],target)
        # print("rotation", rotation)
        # # print("index", index)
        # if(index != -1):return True
        # index = find_in_sorted(nums[rotation:],target)
        # # print("index", index)
        # if(index != -1):return True
        # return False