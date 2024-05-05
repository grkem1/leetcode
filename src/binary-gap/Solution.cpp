// https://leetcode.com/problems/binary-gap

class Solution {
public:
    int binaryGap(int N) {
        int gap = 0;
        int count = 0;
        bool seen = false;
        if( (N & (N-1)) == 0 ){
            return 0;
        }
        while( (N > 0) && (N % 2 == 0) ){
            N/=2;
        }
        while(N > 0){
            int l = N % 2;
            N /= 2;
            if(l == 1){
                gap = max(gap, count + 1);
                count = 0;
            }else{
                count++;
            }
        }
        return gap;
    }
};