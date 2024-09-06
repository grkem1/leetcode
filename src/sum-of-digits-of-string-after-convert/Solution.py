# https://leetcode.com/problems/sum-of-digits-of-string-after-convert

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def tf(i):
            total = 0
            while(i > 0):
                total += i % 10
                i //= 10
            return total

        mapping = {string.ascii_lowercase[i]:i+1 for i in range(26)}
        total = 0
        for l in s:
            total += tf(mapping[l])

        for i in range(1,k):
            if(total < 10): break
            total = tf(total)

        return total
