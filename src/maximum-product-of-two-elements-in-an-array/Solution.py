// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        bests = [0,0]
        for n in nums:
            if(n > bests[0]):
                bests[0],bests[1] = n,bests[0]
            elif(n > bests[1]):
                bests[1] = n
        # print(bests)
        return (bests[0]-1)*(bests[1]-1)