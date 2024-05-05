// https://leetcode.com/problems/subarray-sums-divisible-by-k

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = defaultdict(list)
        total = 0
        for i,n in enumerate(nums):
            total += n
            total %= k
            s[total].append(i)
        # print(s)
        result = 0
        if(len(s[0]) != 0): result += len(s[0])
        total = 0
        for i,n in enumerate(nums):
            total = (total + n) % k
            to_right = 0
            if(len(s[total]) != 0): to_right = len(s[total]) - bisect.bisect(s[total],i)
            # print(i, to_right)
            result += to_right
        return result