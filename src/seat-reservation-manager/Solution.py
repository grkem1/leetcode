// https://leetcode.com/problems/seat-reservation-manager

class SeatManager:

    def __init__(self, n: int):
        self.seat_array = list(range(1,n+1))

    def reserve(self) -> int:
        return heapq.heappop(self.seat_array)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seat_array, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)