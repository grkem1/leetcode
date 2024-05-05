// https://leetcode.com/problems/equal-row-and-column-pairs

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)
        cols = defaultdict(int)
        for i in range(n):
            row = grid[i]
            col = []
            for j in range(n):
                col.append(grid[j][i])
            rows[tuple(row)] += 1
            cols[tuple(col)] += 1
        total = 0
        for r in rows:
            total += cols[r] * rows[r]
        return total