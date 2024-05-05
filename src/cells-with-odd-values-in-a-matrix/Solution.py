// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r_indices = [0]*m
        c_indices = [0]*n
        total = 0
        for i in indices:
            r_indices[i[0]] += 1
            c_indices[i[1]] += 1
        for r in r_indices:
            for c in c_indices:
                total += (r+c)%2
        return total