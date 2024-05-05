// https://leetcode.com/problems/design-circular-queue

class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1]*k
        self.start = 0
        self.size = 0
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        else:
            self.arr[(self.start + self.size) % self.limit] = value
            self.size += 1
            return True
        
    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        else:
            self.start = (self.start + 1) % self.limit
            self.size -= 1
            return True

    def Front(self) -> int:
        if(not self.isEmpty()):
            return self.arr[self.start]
        else:
            return -1

    def Rear(self) -> int:
        if(not self.isEmpty()):
            return self.arr[(self.start + self.size - 1) % self.limit]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit
