// https://leetcode.com/problems/reverse-bits

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t m = 0;
        for(int i = 0; i < 32; i++){
            m <<= 1;
            if( ( ( n >> i ) & 1 ) == 1 ){
                m = m | 1;
            }
        }
        return m;
    }
};