# https://leetcode.com/problems/rearrange-array-elements-by-sign

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = (n for n in nums if n>0)
        neg = (n for n in nums if n<0)
        def generate_list():
            nonlocal pos,neg
            for el in zip(pos,neg):
                yield(el[0])
                yield(el[1])
        return list(generate_list())