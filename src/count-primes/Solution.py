# https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if(n < 3) : return 0
        prime_vector = [False]*2+[True]*(n-2)
        for i in range(2,int(n**0.5)+1):
            for j in range(i**2,n,i):
                prime_vector[j] = False
        # for i,val in enumerate(prime_vector):
            # if(val == True): print(i)
        return prime_vector.count(True)