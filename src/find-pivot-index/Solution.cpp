// https://leetcode.com/problems/find-pivot-index

class Solution {
public:
    vector<int> cumulativeLeft;
    vector<int> cumulativeRight;
    int pivotIndex(vector<int>& nums) {
        if(nums.size() < 1){
            return -1;
        }
        cumulativeLeft.reserve(nums.size());
        cumulativeRight.resize(nums.size());
        cumulativeLeft.push_back(nums[0]);
        cumulativeRight[cumulativeRight.size() - 1] = nums[nums.size() - 1];
        for(int i = 1; i < nums.size(); i++){
            cumulativeLeft.push_back(nums[i] + cumulativeLeft[i-1]);
            cumulativeRight[ cumulativeRight.size() - 1 - i ] = cumulativeRight[ cumulativeRight.size() - i ] + nums[nums.size() - 1 - i];
        }
        for(int i = 0; i < nums.size(); i++){
            if(cumulativeLeft[i] == cumulativeRight[i]){
                return i;
            }
        }
        return -1;
    }
};