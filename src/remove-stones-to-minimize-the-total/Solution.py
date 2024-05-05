// https://leetcode.com/problems/remove-stones-to-minimize-the-total

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        s = 0
        h = []
        for p in piles:
            s += p
            heapq.heappush(h,-p)
        for i in range(k):
            p = -h[0]
            s -= p//2
            p -= p//2
            heapq.heapreplace(h,-p)
        # print(h)
        return s