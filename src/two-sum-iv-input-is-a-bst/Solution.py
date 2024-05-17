# https://leetcode.com/problems/two-sum-iv-input-is-a-bst

class Solution:
    def findTarget(self, root, k: int) -> bool:
        arr = []
        def dfs(r):
            nonlocal arr 
            if(r == None):return
            dfs(r.left)
            arr.append(r.val)
            dfs(r.right)
        dfs(root)
        i,j = 0,len(arr)-1
        while(i<j):
            cur = arr[i]+arr[j]
            if(cur<k):i+=1
            elif(cur>k):j-=1
            else:return True
        return False