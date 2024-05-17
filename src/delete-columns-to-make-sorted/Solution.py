# https://leetcode.com/problems/delete-columns-to-make-sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        total = 0
        for i in range(len(strs[0])):
            last = 0
            for j in range(len(strs)):
                if(ord(strs[j][i]) < last):
                    total+=1
                    break
                last = ord(strs[j][i])
        return total