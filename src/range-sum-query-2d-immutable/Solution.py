# https://leetcode.com/problems/range-sum-query-2d-immutable

import numpy as np
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cum = cum = [list(itertools.accumulate(i)) for i in matrix]
        for i in range(1,len(cum)):
            cum[i] = np.add(cum[i],cum[i-1])
        # print(self.cum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        subtract = 0
        if(row1 > 0):
            if(col1 > 0):
                subtract = self.cum[row1-1][col2] + self.cum[row2][col1-1] - self.cum[row1-1][col1-1]
            else:
                subtract = self.cum[row1-1][col2]
        else:
            if(col1 > 0):
                subtract = self.cum[row2][col1-1]
            # else: subtract = 0, no need
        return (self.cum[row2][col2] - subtract)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)