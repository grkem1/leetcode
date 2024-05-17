# https://leetcode.com/problems/reduce-array-size-to-the-half

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = len(arr)//2
        total = 0
        for i,num_freq in enumerate(collections.Counter(arr).most_common()):
            total += num_freq[1]
            if(total >= count):
                return i+1