// https://leetcode.com/problems/online-stock-span

class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        span = 1
        while(self.arr and price >= self.arr[-1][0]):
            span += self.arr.pop()[1]
        self.arr.append([price,span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)