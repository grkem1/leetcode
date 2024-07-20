# https://leetcode.com/problems/lucky-numbers-in-a-matrix

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        def min_index(iterable):
            m = min(iterable)
            return iterable.index(m)

        def max_index(iterable):
            m = max(iterable)
            return iterable.index(m)
        rows = [min_index(row) for row in matrix]
        columns = [max_index(column) for column in [
            [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]]
        result = []
        for i, r in enumerate(rows):
            if (columns[r] == i):
                result.append(matrix[i][r])
        return result
