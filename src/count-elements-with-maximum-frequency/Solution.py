# https://leetcode.com/problems/count-elements-with-maximum-frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f = collections.Counter(nums)
        total = 0
        occurance = 0
        for el in f.most_common():
            if(total == 0):
                occurance = el[1]
                total += occurance
            else:
                if(el[1] == occurance):
                    total += occurance
                else:
                    break
        return total