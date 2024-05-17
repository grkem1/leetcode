# https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s1)+len(s2)!=len(s3)):
            return False
        if(s1 == "" or s2 == ""):
            return (s1 == s3 or s2 == s3)
        m,n = len(s1)+2,len(s2)+2
        dp = [[False]*n for i in range(m)]
        dp[1][1] = True
        for i in range(1,m):
            for j in range(1,n):
                if(dp[i-1][j] and s1[i-2]==s3[i+j-3] or dp[i][j-1] and s2[j-2]==s3[i+j-3]):
                    dp[i][j] = True
#        print(dp)
        return dp[-1][-1]
