# https://leetcode.com/problems/validate-binary-tree-nodes

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        seen = set()
        q = deque()
        #find head first. multiple heads means no valid tree.
        seen_2 = [False]*n
        for el in leftChild:
            if(el!=-1):seen_2[el] = True
        for el in rightChild:
            if(el!=-1):seen_2[el] = True
        head = -1
        for el,s in enumerate(seen_2):
            if(s == False):
                if(head != -1):
                    return False
                head = el
        if(head == -1): return False
        q.append(head)
        # print(head)
        while(len(q) > 0):
            node = q.popleft()
            if(node in seen):
                # print(node)
                return False
            seen.add(node)
            if(leftChild[node] != -1): q.append(leftChild[node])
            if(rightChild[node] != -1): q.append(rightChild[node])
        return len(seen) == n