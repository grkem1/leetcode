// https://leetcode.com/problems/advantage-shuffle

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        A_perm = [None] * len(A)
        for b_index in range(len(B)):
            a_index = bisect.bisect(A,B[b_index])
            if(a_index == len(A)):
                a_index = 0 # can not beat anyway, take the smallest
            A_perm[b_index] = A[a_index]
            A = A[:a_index] + A[a_index+1:]
        return A_perm