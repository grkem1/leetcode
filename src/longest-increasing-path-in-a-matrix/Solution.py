# https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, matrix: [[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        longest_chains = [[-1]*n for i in range(m)]
        longest_max = 1
        def find_longest_chain(i,j):
            nonlocal longest_max,m,n,longest_chains,matrix
            # if(not -1 < i < m or not -1 < j < n):
            #     return -1 # not even on the matrix
            if(longest_chains[i][j] != -1):
                return longest_chains[i][j]
            longest = 1
            for direction in ((-1,0),(1,0),(0,-1),(0,1)):
                i_,j_ = i+direction[0],j+direction[1]
                if(not -1 < i_ < m or not -1 < j_ < n):
                    continue # not even on the matrix
                if(matrix[i_][j_] > matrix[i][j]): #increasing path
                    longest = max(longest, find_longest_chain(i_,j_)+1)
            longest_chains[i][j] = longest
            longest_max = max(longest,longest_max)
            return longest
        for i in range(m):
            for j in range(n):
                if(longest_chains[i][j] == -1):
                    find_longest_chain(i,j)
        return longest_max        