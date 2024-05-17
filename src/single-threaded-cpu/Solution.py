# https://leetcode.com/problems/single-threaded-cpu

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([t[0],i,t[1]] for i,t in enumerate(tasks))
        # tasks.sort()
        order = []
        q = []
        lo = 0
        hi = 0
        time = tasks[0][0]
        while(hi < len(tasks)):
            hi = bisect.bisect(tasks,[time,10**10],lo=lo)
            if(len(q) == 0 and hi == lo): 
                hi += 1
                time = tasks[lo][0]
                hi = bisect.bisect(tasks,[time,10**10],lo=lo)
            for i in range(lo,hi):
                heapq.heappush(q,tasks[i][::-1])
            t = heapq.heappop(q)
            order.append( t[1] )
            time += t[0]
            # print(t,time)
            lo = hi
        while(len(q)>0):
            t = heapq.heappop(q)
            order.append( t[1] )
        return order