// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for a,b in zip(arr,arr[1:]):
            if(diff != b-a): return False
        return True