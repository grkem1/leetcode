# https://leetcode.com/problems/custom-sort-string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0]*len(order)
        order = {order[i]:i for i in range(len(order))}
        for l in s:
            if(l in order):
                count[order[l]]+=1
            else:
                count.append(1)
                order[l] = len(count)-1
        return ''.join(l*count[order[l]] for l in order)