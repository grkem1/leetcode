// https://leetcode.com/problems/split-linked-list-in-parts

class Solution:
    def splitListToParts(self, head: [ListNode], k: int) -> [[ListNode]]:
        if(head == None):
            return [None]*k
        count = 1 
        dummy = head
        while(dummy.next):
            dummy = dummy.next
            count += 1
#        print(count)
        l_each = count//k
        extras = count - l_each*k
        dummy = head
        rlist = []
        for i in range(k):
            length = l_each + (extras>0) - 1 
            extras-=1
            for j in range(length):
                dummy = dummy.next
            if(head):
                rlist.append(head)
                dummy.next,head,dummy = None,dummy.next,dummy.next
            else:
                rlist.append(None)
        return rlist
