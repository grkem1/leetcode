// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()
        for i,n in enumerate(nums):
            while(i != n-1):
                if(nums[n-1] == n):
                    result.add(n)
                    break
                else:
                    nums[n-1], nums[i] = nums[i], nums[n-1]
                    n = nums[i]
        return list(result)