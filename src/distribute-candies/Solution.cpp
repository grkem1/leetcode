// https://leetcode.com/problems/distribute-candies

class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_set<int> types;
        for(int i = 0; i < candies.size(); i++){
            if( types.find(candies[i]) == types.end() ){
                types.insert(candies[i]);
            }
        }
        return min(candies.size() / 2 , types.size() );
    }
};