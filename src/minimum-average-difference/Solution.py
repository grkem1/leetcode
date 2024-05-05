// https://leetcode.com/problems/minimum-average-difference

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = 0
        acc = []
        for n in nums:
            total += n
            acc.append(total)
        best = 10**5
        best_i = 0
        for i in range(0,len(acc)-1):
            current = abs(acc[i]//(i+1) - (total - acc[i])//(len(nums)-i-1))
            if(current < best):
                best = current
                best_i = i
            print(current,best)
        if(total // len(nums) < best):
            return len(nums)-1
        else:
            return best_i