// https://leetcode.com/problems/palindrome-number

long rev(long x){
    long temp;
    long ret = 0;
    while(x != 0){
        ret = ret * 10;
        temp = x % 10;
        ret = ret + temp;
        x = x / 10;
    }
    return ret;
}

class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0){
            return 0;
        }
        if( rev(x) == x ){
            return 1;
        }else{
            return 0;
        }
    }
};