// https://leetcode.com/problems/peeking-iterator

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.hN  = self.iterator.hasNext()
        self.top = self.iterator.next()

        

    def peek(self):
        return self.top

    def next(self):
        rv = self.top
        self.hN = self.iterator.hasNext()
        self.top = self.iterator.next()
        return rv
        

    def hasNext(self):
        return self.hN
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].