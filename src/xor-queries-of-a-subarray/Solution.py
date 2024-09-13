# https://leetcode.com/problems/xor-queries-of-a-subarray

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = list(itertools.accumulate([0]+arr, lambda x,y: x^y))
        return [prefix[q[1]+1] ^ prefix[q[0]] for q in queries]
