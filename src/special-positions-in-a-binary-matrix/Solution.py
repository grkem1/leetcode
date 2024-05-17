# https://leetcode.com/problems/special-positions-in-a-binary-matrix

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        dp = set()
        def check_col(j):
            nonlocal dp,mat
            if(j in dp):
                return False
            total = 0
            for i in range(len(mat)):
                total += mat[i][j]
                if(total > 1):
                    dp.add(j)
                    return False
            return True
        total = 0
        for i,row in enumerate(mat):
            if(sum(row) == 1):
                j = row.index(1)
                if(check_col(j)):
                    total += 1
        return total