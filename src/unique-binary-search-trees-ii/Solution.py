// https://leetcode.com/problems/unique-binary-search-trees-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> [[TreeNode]]:
        result = []
        seen = set()
        for i in itertools.permutations(range(1,n+1)):
            dummy = TreeNode(0)
            u_id = 0 
            for j in i:
                current = dummy
                multiplier = 10**(j-1)
                level = 1 
                while( (current.left and current.val > j) or (current.right and current.val <= j) ):
                    level += 1
                    if(current.val > j): 
                        current = current.left
                    else:
                        current = current.right
                if(current.val > j): 
                    current.left = TreeNode(j)
                else:
                    current.right = TreeNode(j)
                u_id += multiplier * level
            if(u_id not in seen):
#               print(u_id)
                seen.add(u_id)
                result.append(dummy.right)
        return result