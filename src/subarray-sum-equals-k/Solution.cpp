// https://leetcode.com/problems/subarray-sum-equals-k

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        if(nums.size() < 1){
            return 0;
        }
        long count = 0;
        vector<int> cumulative(nums.size() + 1, 0);
        for(int i = 1; i < nums.size() + 1; i++){
            cumulative[i] = cumulative[i-1] + nums[i-1];
            for(int j = 0; j < i; j++){
                if(cumulative[i] - cumulative[j] == k){
                    count++;
                }
            }
        }
        return count;
    }
};