// https://leetcode.com/problems/merge-k-sorted-lists

class Solution:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        root = ListNode()
        smallest = []
        for i,node in enumerate(lists):
            if(node != None):
                smallest.append([node.val,i])
        heapq.heapify(smallest)
        current = root
        while(len(smallest) > 0):
            val,index = smallest[0]
            node = lists[index]
            lists[index] = node.next
            current.next = node
#            print(val)
#            print(smallest)
            current = current.next
            if(node.next):
                heapq.heapreplace(smallest,[node.next.val,index])
            else:
                heapq.heappop(smallest)
        return root.next
