# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def includes(a, b):
            return a == b[: len(a)] == b[-len(a) :]

        return sum(
            sum(includes(a, b) for b in words[i + 1 :]) for i, a in enumerate(words)
        )
