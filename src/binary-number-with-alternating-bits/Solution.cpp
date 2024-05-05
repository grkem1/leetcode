// https://leetcode.com/problems/binary-number-with-alternating-bits

class Solution {
public:
    bool isPowerofTwo(const long& n){
        if(n < 1){
            return false;
        }
        return ( (n & (n-1)) == 0 );
    }
    long m;
    bool hasAlternatingBits(int n) {
        m = ( n ^ (n >> 1) );
        m++;
        return isPowerofTwo(m);
    }
};