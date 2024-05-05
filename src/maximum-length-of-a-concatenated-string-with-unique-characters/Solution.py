// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def str2tuple(s):
            a = 0
            for l in s:
                if(a & (1 << ord(l)-ord('a')) ):
                    return (0,0)
                a = a | (1 << ord(l) - ord('a'))
            return (len(s),a)
        arr = [str2tuple(s) for s in arr]
        best = 0
        def dfs(i=0,a=0,l=0):
            nonlocal best,arr
            if(i == len(arr)):
                return
            if(arr[i][0] > 0 and arr[i][1] & a == 0):
                best = max(best, l+arr[i][0])
                dfs(i+1,a|arr[i][1],l+arr[i][0])
            dfs(i+1,a,l)
        dfs()
        return best