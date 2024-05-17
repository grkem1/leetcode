# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

class Solution:
    def minPartitions(self, n: str) -> int:
        m = "0"
        for digit in n:
            m = max(digit,m)
        return int(m)