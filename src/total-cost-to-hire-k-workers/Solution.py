# https://leetcode.com/problems/total-cost-to-hire-k-workers

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if(k == len(costs)):
            return sum(costs)
        to_consider = []
        left = candidates
        right = len(costs) - candidates - 1
        if(2*candidates >= len(costs)):
            for i,c in enumerate(costs):
                heapq.heappush(to_consider, (c,i))
            left,right = 1,0
        else:
            for i in range(left):
                heapq.heappush(to_consider, (costs[i],i))
            for i in range(len(costs)-1,right,-1):
                heapq.heappush(to_consider, (costs[i],i))
        total = 0
        for i in range(k):
            # print(to_consider)
            val,index = heapq.heappop(to_consider)
            total += val
            if(index < left):
                if(left <= right):
                    heapq.heappush(to_consider,(costs[left],left))
                left += 1
            else:
                if(left <= right):
                    heapq.heappush(to_consider,(costs[right],right))
                right -= 1
        return total