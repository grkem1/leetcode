# https://leetcode.com/problems/reordered-power-of-2

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        current = 1
        candidates = []
        while(current <= 10**(math.ceil(math.log(n,10)))):
            if(current >= 10**(math.floor(math.log(n,10)))):
                candidates.append(current)
            current *= 2
        def convertable(n_1,n_2):
            arr = [0]*10
            while(n_2 > 0):
                n_2,i = divmod(n_2,10)
                arr[i] += 1
            while(n_1 > 0):
                n_1,i = divmod(n_1,10)
                arr[i] -= 1
            return not any(arr)
        return any(convertable(n,c) for c in candidates)