// https://leetcode.com/problems/longest-harmonious-subsequence

class Solution {
public:
    int findLHS(vector<int>& nums) {
        int count, before, after;
        int neighbor;
        int maxVal = 0;
        unordered_map<int,int> map;
        for(int i = 0; i < nums.size(); i++){
            map[nums[i]]++;
        }
        for(auto it = map.begin(); it != map.end(); it++){
            if(map.find(it->first - 1) != map.end()){
                before = map[it->first - 1];
            }else{
                before = 0;
            }
            if(map.find(it->first + 1) != map.end()){
                after = map[it->first + 1];
            }else{
                after = 0;
            }
            if(before == 0 && after == 0){
                continue;
            }
            int count = max( before, after ) + it->second;
            if( count > maxVal){
                maxVal = count;
            }
        }
        return maxVal;
    }
};