# https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder:

    def __init__(self):
        self.m = [] #median
        self.l = [] #larger
        self.s = [] #smaller

    def addNum(self, num: int) -> None:
        match len(self.m):
            case 0:
                self.m = [num]
            case 1:
                if(num >= self.m[0]):
                    if(len(self.l) == 0 or num <= self.l[0]):
                        self.m.append(num)
                    else:
                        large = heapq.heapreplace(self.l,num)
                        self.m.append(large)
                else:
                    if(len(self.s) == 0 or num > -self.s[0]):
                        self.m = [num,self.m[0]]
                    else:
                        small = heapq.heapreplace(self.s,-num)
                        self.m = [-small,self.m[0]]
            case 2:
                if(num > self.m[1]):
                    heapq.heappush(self.l,num)
                    heapq.heappush(self.s,-self.m[0])
                    self.m = [self.m[1]]
                elif(num < self.m[0]):
                    heapq.heappush(self.s,-num)
                    heapq.heappush(self.l,self.m[1])
                    self.m = [self.m[0]]
                else:
                    heapq.heappush(self.l,self.m[1])
                    heapq.heappush(self.s,-self.m[0])
                    self.m = [num]

    def findMedian(self) -> float:
        return sum(self.m)/len(self.m)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()