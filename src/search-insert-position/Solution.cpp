// https://leetcode.com/problems/search-insert-position

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int begin = 0;
        int end = nums.size() - 1;
        int mid = begin + (end - begin)/2;
        if(target > nums[end]){
            return end + 1;
        }
        if(begin == end){
            return nums[begin] < target ? 1 : 0;
        }
        while(begin != end){
            mid = begin + (end - begin)/2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] > target){
                end = mid;
            }else{
                begin = mid + 1;
            }
        }
        return nums[mid] < target ? mid + 1 : mid;
    }
};