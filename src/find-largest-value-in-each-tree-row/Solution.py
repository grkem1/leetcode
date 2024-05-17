# https://leetcode.com/problems/find-largest-value-in-each-tree-row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []
        q = deque()
        q.append(root)
        q.append(None)
        largests = []
        largest = -2**31
        while(len(q) > 1):
            node = q.popleft()
            if(node == None):
                largests.append(largest)
                largest = -2**31
                q.append(None)
                continue
            largest = max(largest,node.val)
            if(node.left):q.append(node.left)
            if(node.right):q.append(node.right)
        largests.append(largest)
        return largests