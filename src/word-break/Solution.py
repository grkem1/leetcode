// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wD = set(wordDict)
        skip = set()
        def dfs(i):
            nonlocal wD, s
            if(s[i:] in wD):
                return True
            if(s[i:] in skip):
                return False
            for j in range(i+1,len(s)):
                if(s[i:j] in wD and dfs(j)):
                    wD.add(s[i:])
                    return True
            skip.add(s[i:])
            return False
        return dfs(0)