# https://leetcode.com/problems/construct-k-palindrome-strings


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c = collections.Counter(s)
        return len(s) >= k and sum(val % 2 for val in c.values()) <= k
