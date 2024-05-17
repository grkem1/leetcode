# https://leetcode.com/problems/construct-target-array-with-multiple-sums

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if(len(target) == 1): return (target == [1])
        max_heap = [-i for i in target]
        heapq.heapify(max_heap)
        s = sum(target)
        largest = -max_heap[0]
        while(largest > 1):
            inc = s - largest
            # print(largest,inc)
            if(inc == 1): return True
            elif(inc >= largest or inc == 0): return False
            largest,largest_old = (largest % inc),largest
            s += largest - largest_old
            heapq.heapreplace(max_heap,-largest)
            largest = -max_heap[0]
        return True