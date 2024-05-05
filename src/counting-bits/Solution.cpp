// https://leetcode.com/problems/counting-bits

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ones(num + 1, -1);
        ones[0] = 0;
        if(num == 0){
            return ones;
        }
        ones[1] = 1;
        for(int i = 2; i < num + 1; i++){
            ones[i] = ones[i/2] + (i%2);
        }
        return ones;
    }
};