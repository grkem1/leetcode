# https://leetcode.com/problems/my-calendar-i

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        if(len(self.bookings) == 0):
            self.bookings.append((start,end))
            return True
        else:
            right = bisect.bisect(self.bookings,(start,end))
            if(right < len(self.bookings) and self.bookings[right][0] < end):
                return False
            elif(right > 0 and self.bookings[right-1][1] > start):
                return False
            else:
                self.bookings.insert(right,(start,end))
                return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)