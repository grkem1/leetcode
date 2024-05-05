// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = collections.defaultdict(lambda: -1)
        current = 0
        best = 0
        for i,letter in enumerate(s):
            if(last_seen[letter] >= i - current):
                best = max(best, current)
                # print(s[i-current:i])
                current = i - last_seen[letter]
            else:
                current += 1
            last_seen[letter] = i
        best = max(best,current)
        return best