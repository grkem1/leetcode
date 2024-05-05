// https://leetcode.com/problems/power-of-four

class Solution {
public:
    bool isPowerOfFour(int num) {
        if(num < 0){
            return false;
        }
        if(num == 4 || num == 1){
            return true;
        }
        int four = 4;
        for(int i = 0; i < 28; i+=2){
            four = four << 2;
            if( four == num ){
                return true;
            } 
        }
        return false;
    }
};