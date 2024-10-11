# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        targetArrival = times[targetFriend][0]
        times.sort()
        unoccupied = list(range(len(times)))
        occupied = []
        for t in times:
            while(occupied and occupied[0][0] <= t[0]):
                vacant = heapq.heappop(occupied)[1] # newly vacant seat
                heapq.heappush(unoccupied,vacant)   # place it back to unoccupied
            taken = heapq.heappop(unoccupied)       # next arrival takes the smallest seat
            if(t[0] == targetArrival):              # if that is the target (unique), we already know
                return taken                        # which seat it took.
            heapq.heappush(occupied, (t[1], taken)) # "taken" is taken until t[1]
