# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if(k == 1):
            return nums
        last = -1
        skip = -2
        for i in range(1, k):
            if(nums[i] != 1 + nums[i-1]):
                skip = i - 1
        result = []
        for i in range(k-1, len(nums)):
            if(nums[i] != 1 + nums[i-1]):
                result.append(-1)
                skip = i - 1
            elif(i < skip + k):
                result.append(-1)
            else:
                result.append(nums[i])
            # print(skip)
        return result
