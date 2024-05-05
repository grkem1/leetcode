// https://leetcode.com/problems/reverse-integer

long rev(long x){
    long ret = 0;
    long temp;
    while(x != 0){
        ret = ret * 10;
        temp = x % 10;
        ret += temp;
        x = x / 10;
    }
    return ret;
}

class Solution {
public:
    int reverse(int x) {
        long ret = rev(x);
        if(ret < INT_MIN || ret > INT_MAX){
            return 0;
        }
        return (int)ret;
    }
};