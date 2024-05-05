// https://leetcode.com/problems/shuffle-an-array

import random
class Solution:

    def __init__(self, nums: [int]):
        self.n = nums

    def reset(self) -> [int]:
        """ 
        Resets the array to its original configuration and return it.
        """
        return self.n

    def shuffle(self) -> [int]:
        """ 
        Returns a random shuffling of the array.
        """
        return random.sample(self.n,len(self.n))


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()