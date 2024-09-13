# https://leetcode.com/problems/count-the-number-of-consistent-strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(set(w).issubset(allowed) for w in words)
