# https://leetcode.com/problems/binary-trees-with-factors

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        numbers = {x:1 for x in arr}
        total_count = 0
        for head in arr:
            for left in arr:
                if(left > head ** (0.5)): break
                right = head / left
                if(right in numbers):
                    multiplier = 2 if left != right else 1
                    numbers[head] += multiplier * numbers[left] * numbers[right]
            total_count += numbers[head]
        return ( total_count % (10 ** 9 + 7) )