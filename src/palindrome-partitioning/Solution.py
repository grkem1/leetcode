// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> [[str]]:
        return_list = []
        def dfs(arr, remaining):
            nonlocal return_list
            if(remaining == ""):
                return_list.append(arr)
                return
            for end_index in range(1,len(remaining)+1):
                if(remaining[:end_index] == remaining[end_index-1::-1]):
                    dfs(arr+[remaining[:end_index]], remaining[end_index:])
        dfs([],s)
        return return_list