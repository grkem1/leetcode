# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero

class Solution:
    def minOperations(self, nums: [int], x: int) -> int:
        from_left = [0] + list(itertools.accumulate(nums))
        if(from_left[-1] < x):
            return -1
        from_right= [0] + list(itertools.accumulate(nums[::-1]))
        # print(from_left)
        # print(from_right)
        i = 0
        j = len(nums)
        best = len(nums)+1
        while(j >= 0):
            if(from_left[i] + from_right[j] > x):
                j -= 1
            elif(from_left[i] + from_right[j] < x):
                i += 1
            else:
                # print('i: ', i)
                # print('j: ', j)
                best = min(best, i + j)
                i+=1
                j-=1
        if(best > len(nums)):
            return -1
        else:
            return best