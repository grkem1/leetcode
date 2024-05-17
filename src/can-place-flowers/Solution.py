# https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(len(flowerbed)==0): return (n <= 0)
        if(len(flowerbed)==1): return (n <= 1-flowerbed[0])
        count = 0
        if(flowerbed[0:2] == [0,0]):
            flowerbed[0]=1
            count+=1
        if(flowerbed[-2:] == [0,0]):
            flowerbed[-1]=1
            count+=1
        zeros = 0
        i = 1
        while(i < len(flowerbed)-1):
            while(i < len(flowerbed)-1 and flowerbed[i] == 1):
                i+=1
            zeros = 0
            while(i < len(flowerbed)-1 and flowerbed[i] == 0):
                zeros += 1
                i+=1
            if(zeros > 2):
                count += (zeros-1)//2
        return count >= n