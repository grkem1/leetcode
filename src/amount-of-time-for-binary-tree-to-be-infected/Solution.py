// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        neighbors = defaultdict(list)
        def dfs(node,parent=None):
            if(node.right):
                neighbors[node.val].append(node.right.val)
                dfs(node.right,node)
            if(node.left):
                neighbors[node.val].append(node.left.val)
                dfs(node.left,node)
            if(parent):
                neighbors[node.val].append(parent.val)
        dfs(root)
        total = 0
        queue = deque([start,0])
        while(len(queue) > 1):
            # print(queue)
            el = queue.popleft()
            if(el == 0):
                queue.append(0)
                total += 1
                continue
            neighbors[el].append(0)
            for nbor in neighbors[el][:-1]:
                if(neighbors[nbor][-1] != 0):
                    queue.append(nbor)
        return total