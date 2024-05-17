# https://leetcode.com/problems/sort-characters-by-frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        new_s = []
        for el in c.most_common():
            new_s.append(el[1]*el[0])
        return ''.join(new_s)