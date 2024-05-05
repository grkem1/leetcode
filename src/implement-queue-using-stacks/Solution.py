// https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        self.s = []
        self.s_rev = []

    def push(self, x: int) -> None:
        while(len(self.s_rev) > 0):
            self.s.append(self.s_rev.pop())
        self.s.append(x)

    def pop(self) -> int:
        while(len(self.s) > 0):
            self.s_rev.append(self.s.pop())
        return self.s_rev.pop()

    def peek(self) -> int:
        while(len(self.s) > 0):
            self.s_rev.append(self.s.pop())
        return self.s_rev[-1]

    def empty(self) -> bool:
        return (len(self.s)+len(self.s_rev) == 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()