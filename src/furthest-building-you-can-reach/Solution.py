// https://leetcode.com/problems/furthest-building-you-can-reach

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if(len(heights) == 1): return 0
        use_ladder = [0] * ladders
        for i, h in enumerate(heights[:-1]):
            if(heights[i+1] > h):
                if(ladders > 0 and heights[i+1] - h > use_ladder[0]):
                    bricks -= heapq.heapreplace(use_ladder, heights[i+1] - h)
                else:
                    bricks -= (heights[i+1]-h)
                if(bricks < 0):
                    return i
        return i+1