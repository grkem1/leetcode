# https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        lcs = [[0]*(n+1) for i in range(m+1)]
        # print(lcs)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(word1[i-1] == word2[j-1]):
                    # print(i,j)
                    lcs[i][j] = lcs[i-1][j-1]+1
                else:
                    lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])

        # print(lcs)
        best = lcs[-1][-1]
        return m + n - 2 * best