// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        counts = sorted(c.values())
        for i,el in enumerate(counts):
            if(k > el):
                k -= el
            elif(k < el):
                return len(counts) - i
            else:
                return len(counts) - i - 1