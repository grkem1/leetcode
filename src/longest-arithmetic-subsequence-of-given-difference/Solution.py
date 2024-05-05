// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen = defaultdict(int)
        for el in arr:
            seen[el] = max(1,seen[el], seen[el-difference]+1)
        return max(seen.values())