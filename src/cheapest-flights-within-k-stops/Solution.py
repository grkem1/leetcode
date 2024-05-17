# https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = [(0,src,0)]
        best_price_hop = [(2**32,n) for i in range(n)]
        best_price_hop[src] = (0,0)
        adj_list = [[] for i in range(n)]
        for f in flights:
            adj_list[f[0]].append((f[2],f[1]))
        # print(adj_list)
        best = 2**32
        while(len(q) > 0):
            # print(q)
            cheapest = heapq.heappop(q)
            if(cheapest[-1] > k): continue
            if(cheapest[0] >= best - 1): # no negative-cost flight, take the best until now
                return best
            for nbor in adj_list[cheapest[1]]:
                if(nbor[1] == dst):
                    best = min(best,nbor[0]+cheapest[0])
                if(best_price_hop[nbor[1]][0] < cheapest[0]+nbor[0] and best_price_hop[nbor[1]][1] < cheapest[-1]+1):
                    continue
                best_price_hop[nbor[1]] = (nbor[0]+cheapest[0], cheapest[-1]+1)
                heapq.heappush(q,(nbor[0]+cheapest[0],nbor[1],cheapest[-1]+1))
        if(best != 2**32):
            return best
        else:
            return -1