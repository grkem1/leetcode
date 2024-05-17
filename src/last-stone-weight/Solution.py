# https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        stones.sort()
        while(len(stones) > 1):
            # print(stones)
            y = stones.pop()
            x = stones.pop()
            y_new = y - x
            if(y_new != 0):
                new_position = bisect.bisect(stones,y_new)
                stones = stones[:new_position] + [y_new] + stones[new_position:]
        if(len(stones) > 0):
            return stones[0]
        else:
            return 0