// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int current = INT_MAX;
        for(int i = 0; i < nums.size();){
            if(nums[i] != current){
                current = nums[i];
                ++i;
            }else{
                nums.erase( nums.begin() + i );
            }
        }
        return nums.size();
    }
};