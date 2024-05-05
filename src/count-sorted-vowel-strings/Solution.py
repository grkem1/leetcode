// https://leetcode.com/problems/count-sorted-vowel-strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        ends_with = [1]*5
        for i in range(n-1):
            for j in range(1,5):
                ends_with[j] = ends_with[j] + ends_with[j-1]
        # print(ends_with)
        return sum(ends_with)