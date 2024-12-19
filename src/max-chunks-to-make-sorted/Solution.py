# https://leetcode.com/problems/max-chunks-to-make-sorted


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        highest = -1
        for i, n in enumerate(arr):
            highest = max(n, highest)
            if highest == i:
                chunks += 1
        return chunks
