// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m,n = len(matrix),len(matrix[0])
        # # search row
        # i,j = 0,m-1
        # while(i < j):
        #     mid = (i + j + 1) // 2
        #     if(matrix[mid][0] > target):
        #         j = mid - 1
        #     else:
        #         i = mid
        # # i == j == row, search column
        # col = bisect.bisect_left(matrix[i],target)
        # return col < n and matrix[i][col] == target
        pos = bisect.bisect_left([el for r in matrix for el in r],target)
        m,n = len(matrix),len(matrix[0])
        row,col = divmod(pos,n)
        return (row < m and matrix[row][col] == target)