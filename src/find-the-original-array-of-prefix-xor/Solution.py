// https://leetcode.com/problems/find-the-original-array-of-prefix-xor

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [None]
        arr[0] = pref[0]
        for a,b in zip(pref,pref[1:]):
            arr.append(a ^ b)
        return arr