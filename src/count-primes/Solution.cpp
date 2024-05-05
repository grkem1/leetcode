// https://leetcode.com/problems/count-primes

class Solution {
public:
    int countPrimes(int n) {
        if(n < 2){
            return 0;
        }
        vector<bool> isPrime(n, true);
        isPrime[0] = isPrime[1] = false;
        int count = 0;
        for(int i = 2; i < n; i++){
            if(isPrime[i] == true){
                count++;
                for(int j = i; j < n; j+=i){
                    isPrime[j] = false;
                }
            }else{
                
            }
        }
        return count;
    }
};