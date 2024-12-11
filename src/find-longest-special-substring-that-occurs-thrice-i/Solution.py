# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i


class Solution:
    def maximumLength(self, s: str) -> int:
        last_str = ["#", 1]
        longest = -1
        d = defaultdict(int)
        for l in s:
            if last_str[0] == l:
                last_str[1] += 1
            else:
                last_str = [l, 1]
            for i in range(last_str[1], 0, -1):
                d[(last_str[0], i)] += 1
                if d[(last_str[0], i)] >= 3:
                    longest = max(longest, i)
                    break
        return longest
