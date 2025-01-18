# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        level = [(0, 0)]
        next_level = []

        def traverse(i, j):
            nonlocal grid, m, n, seen, next_level
            if not 0 <= i <= m - 1 or not 0 <= j <= n - 1 or (i, j) in seen:
                return
            seen.add((i, j))
            if grid[i][j] == 1:
                traverse(i, j + 1)
            elif grid[i][j] == 2:
                traverse(i, j - 1)
            elif grid[i][j] == 3:
                traverse(i + 1, j)
            else:
                traverse(i - 1, j)
            next_level.append((i, j + 1))
            next_level.append((i, j - 1))
            next_level.append((i + 1, j))
            next_level.append((i - 1, j))

        cost = -1
        while (m - 1, n - 1) not in seen:
            for cell in level:
                traverse(cell[0], cell[1])
            level = next_level
            next_level = []
            cost += 1
        return cost
