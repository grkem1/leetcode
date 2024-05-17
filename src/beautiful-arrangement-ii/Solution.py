# https://leetcode.com/problems/beautiful-arrangement-ii

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        return_array = [1] + [None]*(n-1)
        jump = n-1
        direction = 1
        i = -1
        for i in range(k-1):
            return_array[i+1] = direction*jump + return_array[i]
            direction = -direction
            jump-=1
        for j in range(i+2,n):
            return_array[j] = return_array[j-1] + direction
        return return_array