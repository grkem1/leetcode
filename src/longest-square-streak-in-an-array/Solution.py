# https://leetcode.com/problems/longest-square-streak-in-an-array

# First solution that I could think of involved sorting - O(nlogn) -
# I was using a dictionary like a set, so I thought about making better
# use of the values, to use them as the depth... Second solution is O(n)

# class Solution:
#     def longestSquareStreak(self, nums: List[int]) -> int:
#         d = dict((n,0) for n in sorted(nums))
#         best = 1
#         for n in d:
#             current = 1
#             d[n] = 1
#             while ((n:=n**2) in d and not d[n]):
#                 current += 1
#                 d[n] = 1
#             best = max(best,current)
#         return best if best > 1 else -1

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        d = dict((n,0) for n in nums)
        best = 1
        def dfs(n):
            nonlocal d, best
            if(d[n]):
                return d[n]
            if(n ** 2 in d):
                d[n] = dfs(n**2) + 1
                best = max(best, d[n])
            else:
                d[n] = 1
            return d[n]
        for n in nums:
            dfs(n)
        return best if best !=1 else -1
