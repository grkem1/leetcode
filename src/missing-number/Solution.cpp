// https://leetcode.com/problems/missing-number

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int result = 0;
        for(int& i:nums){
            result ^= i;
        }
        for(int i = 0; i <= nums.size(); i++){
            result ^= i;
        }
        return result;
    }
};