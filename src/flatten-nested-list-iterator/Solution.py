# https://leetcode.com/problems/flatten-nested-list-iterator

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
#         self.n = nestedList
#         self.index = [0]
#         a = self.n[0]
#         while(not a.isInteger()):
#             self.index += [0]
#             a = a.getList()[0]
        self.n = nestedList
        self.index = -1
        self.l = []
        def traverse(nl):
            for el in nl:
                if(el.isInteger()):
                    self.l += [el]
                else:
                    traverse(el.getList())
        return traverse(self.n)
                
    
    def next(self) -> int:
        # a = self.n[self.index[0]]
        # for i in range(1,len(self.index)-1):
        #     a = a.getList()[self.index[i]]
        # if(len(a)-1 > self.index[-1]): # if next is in the same list
        #     self.index[-1] += 1
        #     a = a[self.index[-1]]
        #     while(not a.isInteger()):
        #         a = a.getList()[0]
        #         self.index += [0]
        #     return a
        # else:
        #     self.index.pop()
        self.index += 1
        return self.l[self.index]
            
        
    
    def hasNext(self) -> bool:
        return self.index + 1 < len(self.l)         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())