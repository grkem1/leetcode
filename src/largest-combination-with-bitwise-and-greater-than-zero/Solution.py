# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = defaultdict(int)
        for c in candidates:
            i = 0
            while(c >= 2**i):
                if(c & 2**i):
                    bits[i] += 1
                i += 1
        return max(bits.values())
