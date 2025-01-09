# https://leetcode.com/problems/string-matching-in-an-array


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = set()
        for w in words:
            for i in range(len(w)):
                for j in range(i, len(w)):
                    if i == 0 and j == len(w) - 1:
                        continue
                    substrings.add(w[i : j + 1])
        result = []
        # print(substrings)
        for w in words:
            if w in substrings:
                result.append(w)
        return result
