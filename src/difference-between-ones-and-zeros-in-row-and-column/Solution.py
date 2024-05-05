// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        onesRow = []
        onesCol = []
        for i in range(m):
            onesRow.append(sum(grid[i]))
        for j in range(n):
            Col_j = 0
            for i in range(m):
                Col_j += grid[i][j]
            onesCol.append(Col_j)
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2*(onesRow[i]+onesCol[j]) - m - n
        return grid