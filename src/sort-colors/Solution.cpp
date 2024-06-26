// https://leetcode.com/problems/sort-colors

class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> count(3,0);
        for(int i = nums.size() - 1; i >= 0; i--){
            count[nums[i]]++;
        }
        for(int i = 0; i < count[0]; i++){
            nums[i] = 0;
        }
        for(int i = count[0]; i < count[0] + count[1]; i++){
            nums[i] = 1;
        } 
        for(int i = count[0] + count[1]; i < nums.size(); i++){
            nums[i] = 2;
        }
        // return nums;
    }
};