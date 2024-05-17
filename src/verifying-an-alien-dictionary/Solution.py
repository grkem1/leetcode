# https://leetcode.com/problems/verifying-an-alien-dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = dict()
        for i in range(ord('a'),ord('z')+1):
            mapping[order[i - ord('a')]] = chr(i)
        # print(mapping)
        def convert(w):
            nonlocal mapping
            letters = []
            for l in w:
                letters.append(mapping[l])
            return ''.join(letters)
        words = [convert(w) for w in words]
        # print(words)
        return words == sorted(words)