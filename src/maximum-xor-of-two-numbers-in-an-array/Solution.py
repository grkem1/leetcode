# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

class Solution:
    def findMaximumXOR(self, a: List[int]) -> int:
        class Node:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
        root = Node()
        for number in a:
            current = root
            original = number
            for i in range(32):
                if(number & 2**31):
                    if(current.right == None):
                        current.right = Node()
                    current = current.right
                else:
                    if(current.left == None):
                        current.left = Node()
                    current = current.left
                number = number << 1
            current.val = original
        def dfs_print(n):
            if(n == None):
                return
            dfs_print(n.left)
            print(n.val)
            dfs_print(n.right)
        #dfs_print(root)
        best = 0
        for number in a:
            target = root
            original = number
            for i in range(32):
                if(number & 2**31):
                    if(target.left):
                        target = target.left
                    else:
                        if(target.right == None):
                            best = max(best,original ^ target.val)
                            break
                        target = target.right
                else:
                    if(target.right):
                        target = target.right
                    else:
                        if(target.left == None):
                            best = max(best,original ^ target.val)
                            break
                        target = target.left
                # print(number)
                number = number << 1
            while(target):
                if(target.right):
                    target = target.right
                else:
                    if(target.left):
                        target = target.left
                    else:
                        best = max(best,original ^ target.val)
                        break
        return best