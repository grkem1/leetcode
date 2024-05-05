// https://leetcode.com/problems/shift-2d-grid

class Solution:
    def shiftGrid(self, grid: [[int]], k: int) -> [[int]]:
        m,n = len(grid),len(grid[0])
        def row_column(i):
            nonlocal m,n
            i = i % (m*n)
            return divmod(i,n)
        k = k % (m*n)
        if(k == 0):
            return grid
        elements = list(itertools.chain(*grid))
        for i,el in enumerate(elements):
            # print(el)
            r,c = row_column(i+k)
            grid[r][c] = el
        return grid