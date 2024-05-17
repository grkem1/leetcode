# https://leetcode.com/problems/build-an-array-with-stack-operations

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_i = 0
        last = 1
        operations = []
        while(target_i < len(target)):
            while(target[target_i] > last):
                operations.append('Push')
                last += 1
                operations.append('Pop')
            operations.append('Push')
            last += 1
            target_i += 1
        return operations