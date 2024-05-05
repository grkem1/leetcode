// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> result;
        result.reserve(2);
        int i,j;
        j = 1;
        for(i = 0; i < numbers.size() && numbers[i] <= target/2; i++ ){
            
            while( j < numbers.size() && numbers[j] < target - numbers[i] ){
                j++;
            }
            if(j == numbers.size()){
                j = i + 2;
                continue;
            }
            if( numbers[j] + numbers[i] == target ){
                result.push_back(++i);
                result.push_back(++j);
                return result;    
            }
            while( j > 0 && numbers[j] > target - numbers[i+1]){
                j--;
            }
        }
        return result;
    }
};