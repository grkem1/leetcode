// https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s = [root]
        dummy = root.left
        while(dummy):
            self.s.append(dummy)
            dummy = dummy.left

    def next(self) -> int:
        n = self.s.pop()
        dummy = n.right
        while(dummy):
            self.s.append(dummy)
            dummy = dummy.left
        return n.val

    def hasNext(self) -> bool:
        return len(self.s) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()