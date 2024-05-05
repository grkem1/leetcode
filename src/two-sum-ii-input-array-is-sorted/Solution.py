// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        i,j = 0,len(numbers)-1
        while(i < j):
            if(numbers[i] + numbers[j] < target):
                i += 1
            elif(numbers[i] + numbers[j] > target):
                j -= 1
            else:
                return [i+1,j+1]
        return -1