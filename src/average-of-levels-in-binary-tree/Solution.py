// https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = collections.deque([root,None])
        avgs = []
        current_sum = 0
        current_count = 0
        while(len(level) > 0):
            n = level.popleft()
            if(n == None):
                if(current_count == 0):
                    return avgs
                else:
                    avgs.append(current_sum/current_count)
                    current_sum = current_count = 0
                    level.append(None)
            else:
                current_sum += n.val
                current_count += 1
                if(n.left): level.append(n.left)
                if(n.right): level.append(n.right)