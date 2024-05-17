# https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        elements = Counter(arr)
        return len(set(elements.values())) == len(elements)