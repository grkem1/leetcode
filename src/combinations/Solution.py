// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if(k == 1):
            return list([i] for i in range(1,n+1))
        if(n == k):
            return [list(range(1,n+1))]
        if(n < k):
            return []
        res = list(i + [n] for i in self.combine(n-1,k-1))
        # res = []
        # for el in self.combine(n-1,k-1):
        #     print(el)
        #     res.append(el + list(range(n,n+1)))
        res = res + self.combine(n-1,k)
        return res