# https://leetcode.com/problems/range-sum-query-immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.cums = nums
        for i in range(1,len(self.cums)):
            self.cums[i] = self.cums[i-1]+self.cums[i]

    def sumRange(self, left: int, right: int) -> int:
        if(left==0): return self.cums[right]
        return self.cums[right] - self.cums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)