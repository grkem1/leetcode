# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        seen = defaultdict(int)
        for el in arr:
            # print("el before", el)
            el %= k
            # print("el after", el)
            if( seen[(k - el) % k] > 0):
                seen[(k-el)%k] -= 1
            else:
                seen[el] += 1
        # print("seen values", seen.values())
        return sum(seen.values()) == 0
