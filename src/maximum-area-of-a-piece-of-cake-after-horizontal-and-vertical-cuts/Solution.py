// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts+=[0,h]
        verticalCuts+=[0,w]
        horizontalCuts.sort()
        verticalCuts.sort()
        h_max = max((j-i) for i,j in zip(horizontalCuts,horizontalCuts[1:]))
        v_max = max((j-i) for i,j in zip(verticalCuts,verticalCuts[1:]))
        return (v_max*h_max)%(10**9+7)