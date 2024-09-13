# https://leetcode.com/problems/spiral-matrix-iv

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for i in range(m)]
        left, right, up, down = 0, n-1, 0, m-1
        pos = [0,0]
        ptr = head
        i = 0
        matrix[pos[0]][pos[1]] = ptr.val
        while(ptr.next):
            match i:
                case 0:
                    if(pos[1] < right):
                        pos[1] += 1
                        ptr = ptr.next
                    else:
                        i = (i + 1) % 4
                        up += 1
                case 1:
                    if(pos[0] < down):
                        pos[0] += 1
                        ptr = ptr.next
                    else:
                        i = (i + 1) % 4
                        right -= 1
                case 2:
                    if(pos[1] > left):
                        pos[1] -= 1
                        ptr = ptr.next
                    else:
                        i = (i + 1) % 4
                        down -= 1
                case 3:
                    if(pos[0] > up):
                        pos[0] -= 1
                        ptr = ptr.next
                    else:
                        i = (i + 1) % 4
                        left += 1
            matrix[pos[0]][pos[1]] = ptr.val
        return matrix
