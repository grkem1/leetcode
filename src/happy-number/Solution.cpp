// https://leetcode.com/problems/happy-number

class Solution {
public:
    int next(int n){
        int rv = 0;
        while(n != 0){
            rv += pow( (n % 10), 2 );
            n /= 10;
        }
        return rv;
    }
    bool isHappy(int n) {
        unordered_set<int> seen;
        while( seen.find(n) == seen.end() && n != 1 ){
            seen.insert(n);        
            n = next(n);
        }
        if(n == 1){
            return true;
        }
        return false;
    }
};