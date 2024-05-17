# https://leetcode.com/problems/maximum-length-of-pair-chain

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        i = 0
        last = [-1001,-1001]
        total = 1
        valid = True
        while(i < len(pairs) and valid):
            valid = False
            for j in range(i+1, len(pairs)):
                if(pairs[i][1] > pairs[j][1]):
                    i = j
                    valid = True
                else:
                    if(pairs[i][1] < pairs[j][0]):
                        total += 1
                        i = j
                        valid = True
                    else:
                        pass
        return total