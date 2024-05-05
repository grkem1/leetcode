// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i[1] for i in sorted( (sum(r),i) for i,r in enumerate(mat))][:k]
