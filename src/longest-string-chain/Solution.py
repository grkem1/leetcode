// https://leetcode.com/problems/longest-string-chain

class Solution:
    def longestStrChain(self, words:[str]) -> int:
        def isPred(word1,word2):
            # print(word1,word2)
            if(len(word1) != len(word2)-1):
                return False
            offset = 0
            for i in range(len(word1)):
                if(word1[i] != word2[i+offset]):
                    if(offset != 0):
                        return False
                    else:
                        offset = 1 #skip one letter in word2
                        if(word1[i] != word2[i+offset]):
                            return False
            return True
        words.sort(key=lambda w:len(w))
        # print(words)
        dp = [1]*len(words)
        best = 1
        for i in range(len(words)-1,0,-1):
            for j in range(i-1,-1,-1):
                if(isPred(words[j],words[i])):
                    dp[j] = max(dp[j],dp[i]+1)
                    # if(dp[j] > best):
                        # print(words[i],words[j])
                    best = max(dp[j],best)
        # print(dp)
        return best