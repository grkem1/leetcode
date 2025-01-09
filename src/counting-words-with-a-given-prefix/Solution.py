# https://leetcode.com/problems/counting-words-with-a-given-prefix


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)
