# https://leetcode.com/problems/design-a-stack-with-increment-operation

class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = [0]*maxSize
        self.idx = -1

    def push(self, x: int) -> None:
        if(self.idx < len(self.arr) - 1):
            self.idx += 1
            self.arr[self.idx] = x

    def pop(self) -> int:
        if(self.idx > -1):
            rv = self.arr[self.idx]
            self.idx -= 1
            return rv
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.idx+1)):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
