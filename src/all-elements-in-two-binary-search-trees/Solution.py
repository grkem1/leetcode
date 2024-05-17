# https://leetcode.com/problems/all-elements-in-two-binary-search-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = []
        list2 = []
        listall = []
        def traverse(r,l):
            if(r == None):return
            traverse(r.left,l)
            l.append(r.val)
            traverse(r.right,l)
        traverse(root1,list1)
        traverse(root2,list2)
        i,j = 0,0
        while(True):
            if(i == len(list1)):
                return listall+list2[j:]
            if(j == len(list2)):
                return listall+list1[i:]
            if(list1[i] < list2[j]):
                listall.append(list1[i])
                i+=1
            else:
                listall.append(list2[j])
                j+=1
        return listall