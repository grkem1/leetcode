// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r,c = len(matrix),len(matrix[0])
        cumulative = [[0 for i in range(c)] for j in range(r)]
        cumulative[0][0] = matrix[0][0]
        for i in range(1,c): cumulative[0][i] = cumulative[0][i-1] + matrix[0][i]
        for i in range(1,r): cumulative[i][0] = cumulative[i-1][0] + matrix[i][0]
        for i in range(1,c):
            for j in range(1,r):
                cumulative[j][i] = matrix[j][i] + cumulative[j-1][i] + cumulative[j][i-1] - cumulative[j-1][i-1]
        def submatrix_sum(r1,r2,c1,c2): # endpoints inclusive
            # if(r1 > r2 or c1 > c2): print("something's wrong")
            if(r1 == 0 and c1 == 0): return cumulative[r2][c2]
            if(r1 == 0 and c1 != 0): return cumulative[r2][c2] - cumulative[r2][c1-1]
            if(r1 != 0 and c1 == 0): return cumulative[r2][c2] - cumulative[r1-1][c2]
            return cumulative[r2][c2] - cumulative[r1-1][c2] - cumulative[r2][c1-1] + cumulative[r1-1][c1-1]
        count = 0
        for r1 in range(r):
            for r2 in range(r1,r):
                windows = {0:1}
                window = 0
                for c1 in range(c):
                    window += submatrix_sum(r1,r2,c1,c1)
                    if( (window-target) in windows ):
                        count += windows[window-target]
                        # print(r1,r2,c1)
                    if(window in windows):
                        windows[window] += 1
                    else:
                        windows[window] = 1
        return count