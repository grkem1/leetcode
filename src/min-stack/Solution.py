# https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.a = []
        self.mins = [2**32]

    def push(self, val: int) -> None:
        self.a.append(val)
        self.mins.append(min(self.mins[-1],val))
        
    def pop(self) -> None:
        self.mins.pop()
        return self.a.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()