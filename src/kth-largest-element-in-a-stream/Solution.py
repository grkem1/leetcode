// https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        self.nums = sorted(nums)[-k:] # largest k are important, ignore the rest

    def add(self, val: int) -> int:
        n = self.nums
        if(len(n) < self.k):
            heapq.heappush(n,val)
            return n[0]
        elif(n[0] >= val):
            return n[0]
        else:
            heapq.heapreplace(n,val)
            return n[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)